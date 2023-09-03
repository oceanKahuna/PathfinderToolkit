from typing import Any, Optional
from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(Character)
admin.site.register(Inventory)

admin.site.unregister(User)

from django.contrib.auth.admin import UserAdmin 
@admin.register(User) 
class NewAdmin(UserAdmin): 
    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form 
    
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','weight_lbs', 'value_in_gold')
    search_fields = ('name__startswith',)