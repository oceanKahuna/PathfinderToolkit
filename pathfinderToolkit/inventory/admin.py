from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ItemCategory)
admin.site.register(Item)
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(Character)
admin.site.register(Inventory)
