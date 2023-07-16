from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index),
    path('item/', views.item_form_view),
]