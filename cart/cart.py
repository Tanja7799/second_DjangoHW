

from decimal import Decimal
from django.conf import settings
from car_project.models import Car

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, car, quantity=1, update_quantity=False):
        car_id = str(car.id)
        if car_id not in self.cart:
            self.cart[car_id] = {'quantity': 0, 'price': str(car.price)}
        if update_quantity:
            self.cart[car_id]['quantity'] = quantity
        else:
            self.cart[car_id]['quantity'] += quantity
        self.save()

    def save(self):
        for item in self.cart.values():
            if isinstance(item['price'], Decimal):
                item['price'] = str(item['price'])
            item['quantity'] = int(item['quantity'])
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True



    def remove(self, car):
        car_id = str(car.id)
        if car_id in self.cart:
            del self.cart[car_id]
            self.save()

    def update(self, car, quantity):
        car_id = str(car.id)
        if car_id in self.cart:
            self.cart[car_id]['quantity'] = quantity
            self.save()

    def __iter__(self):
        car_ids = self.cart.keys()
        cars = Car.objects.filter(id__in=car_ids)
        for car in cars:
            self.cart[str(car.id)]['car'] = car

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['quantity'] = int(item['quantity'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return str(sum(item['quantity'] for item in self.cart.values()))

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()


