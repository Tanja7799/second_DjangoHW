from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:car_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:car_id>/', views.cart_remove, name='cart_remove'),
    path('update/<int:car_id>/<int:quantity>/', views.cart_update, name='cart_update'),

]