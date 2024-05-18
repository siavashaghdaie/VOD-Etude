from django.contrib import admin
from django.urls import path, include
from jjii import views


urlpatterns = [
    path('', views.home , name = 'home'),
    path('slider-form/', views.slideUpdate , name = 'slider-form'),
    path('exclusive/', views.exclusive , name = 'exclusive'),
    path('message/', views.message , name='message')
]