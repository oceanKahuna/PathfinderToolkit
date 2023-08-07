from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index),
    path('item/', views.item_form_view),
    path('about', views.about),
    path('item/all_items', views.all_items),
    path('home/', views.home, name='home'), 
    path('register/', views.register, name='register'),  
    path('login/', views.login, name='login'),
]