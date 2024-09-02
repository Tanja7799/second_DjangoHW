from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from car_project.models import Car

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def cart_add(request, car_id):
    cart = Cart(request)
    car = get_object_or_404(Car, id=car_id)
    cart.add(car=car)
    return redirect('cart_detail')

def cart_remove(request, car_id):
    cart = Cart(request)
    car = get_object_or_404(Car, id=car_id)
    cart.remove(car)
    return redirect('cart_detail')

def cart_update(request, car_id, quantity):
    cart = Cart(request)
    car = get_object_or_404(Car, id=car_id)
    cart.update(car=car, quantity=quantity)
    return redirect('cart_detail')

