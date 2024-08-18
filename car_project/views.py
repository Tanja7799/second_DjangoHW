

from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def car_list(request):
    cars = Car.objects.all().order_by('id')
    paginator = Paginator(cars, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'car_project/car/car_list.html', {'cars': page, 'page': page})


def car_detail(request, slug):
    car = get_object_or_404(Car, slug=slug)
    return render(request, 'car_project/car/car_detail.html', {'car': car})
