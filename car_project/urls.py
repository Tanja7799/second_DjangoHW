from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<slug:slug>', views.car_detail, name='car_detail'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('comments/', views.comment_list, name='comment_list'),

]
