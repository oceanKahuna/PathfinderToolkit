from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view 
from .serializers import ItemSerializer
from rest_framework import generics
from inventory.models import Item
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(['GET'])
def items(request):
    items = Item.objects.all()
    serialized_item = ItemSerializer(items, many=True)
    return Response(items.values())

class ItemsView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class SingleItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    