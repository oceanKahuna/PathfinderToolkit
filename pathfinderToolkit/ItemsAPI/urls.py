from django.urls import path
from . import views 

urlpatterns = [
    path('items/',views.ItemsView.as_view()),
    path('items/<int:pk>',views.SingleItemView.as_view())
]