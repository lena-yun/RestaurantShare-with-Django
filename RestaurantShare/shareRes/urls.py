from django.contrib import admin
from django.urls import path, include
from shareRes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail/', views.restaurantDetail, name='restaurantDetail'),
    path('restaurantCreate/', views.restaurantCreate, name='restaurantCreate'),
    path('categoryCreate/', views.categoryCreate, name='categoryCreate'),

]