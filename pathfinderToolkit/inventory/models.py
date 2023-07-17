from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=50)
    characterLevel = models.IntegerField(validators=[MaxValueValidator(40)])
    experience = models.DecimalField(max_digits=7,decimal_places=2)

class ItemCategory(models.Model):
    item_category_name = models.CharField(max_length=100,unique=True)

class Item(models.Model):
    name = models.CharField(max_length=50,unique=True)
    weight_lbs = models.DecimalField(max_digits=6,decimal_places=2)
    value_in_gold = models.DecimalField(max_digits=20,decimal_places=2)
    source = models.CharField(max_length=200, null=True, blank=True)
    category_id = models.ForeignKey(ItemCategory, on_delete = models.PROTECT, default=None, related_name = 'item_category')

class Weapon(Item):
    damage = models.IntegerField()
    critical = models.IntegerField() 
    CATEGORY_CHOICES = [
        ('light', _('Light')),
        ('one_handed',_('one-handed')),
        ('two_handed',_('two_handed')),
    ]
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    PROFICIENCY_CHOICES = [
    ('martial',_('Martial')),
    ('simple',_('Simple')),
    ('exotice',_('Exotic'))
    ]
    proficiency = models.CharField(choices=PROFICIENCY_CHOICES, max_length=20)

class Armor(Item):
    armor_bonus = models.IntegerField()
    max_dex_bonus = models.IntegerField()
    arcane_spell_failure_percent_chance = models.IntegerField()
    speed_base_30 = models.IntegerField(null=True, blank=True)
    speed_base_20 = models.IntegerField(null=True, blank=True)

class Inventory(models.Model):
    character = models.ForeignKey(Character,on_delete=models.CASCADE, related_name = 'inventory')
    item_id = models.ForeignKey(Item, on_delete=models.PROTECT, related_name='item')
    slots = models.IntegerField()