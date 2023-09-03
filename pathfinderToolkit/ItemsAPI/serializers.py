from rest_framework import serializers
from inventory.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item 
        fields = ['id','name','weight_lbs','value_in_gold','source','item_category']