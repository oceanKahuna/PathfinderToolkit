from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

# Create your models here.

class Character(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True)
    characterLevel = models.IntegerField(validators=[MaxValueValidator(40)])
    experience = models.DecimalField(max_digits=7,decimal_places=2)
    def __str__(self): 
        return f"{self.first_name} {self.last_name}"
    def characters(self):
        return Character.objects.all()

class Item(models.Model):
    name = models.CharField(max_length=50,unique=True)
    weight_lbs = models.DecimalField(max_digits=6,decimal_places=2)
    value_in_gold = models.DecimalField(max_digits=20,decimal_places=2)
    source = models.CharField(max_length=200, null=True, blank=True)

    item_category_choices = [('weapon',_('Weapon')),
                            ('armor',_('Armor')),]
    item_category = models.CharField(choices = item_category_choices, max_length = 50,null=True)
    def __str__(self): 
        return f"{self.name}" 
    def items(self):
        return Item.objects.all()

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