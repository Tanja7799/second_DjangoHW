from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<slug:slug>', views.car_detail, name='car_detail'),

]
