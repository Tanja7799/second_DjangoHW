from django.urls import path
from . import views
from .views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [

    path('car/<slug:slug>', CarDetailView.as_view(), name='car_detail'),
    path('car/new/', CarCreateView.as_view(), name='car_create'),
    path('car/<slug:slug>/edit/', CarUpdateView.as_view(), name='car_update'),
    path('car/<slug:slug>/delete/', CarDeleteView.as_view(), name='car_delete'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('comments/', views.comment_list, name='comment_list'),
    path('', CarListView.as_view(), name='car_list'),
]