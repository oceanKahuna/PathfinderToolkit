from django import forms
from django.forms.widgets import NumberInput

SEXES = (
    ('male','Male'),
    ('female','Female'),
    ('undefined','Undefined'),
    ('other','Other'),
    ('intersex','Intersex')
)

class namesInput(forms.Form):
    player_first_name = forms.CharField(max_length=20)
    player_last_name = forms.CharField(max_length=20)
    character_first_name = forms.CharField(max_length=20)
    character_last_name = forms.CharField(max_length=20)
    sex = forms.ChoiceField(choices=SEXES)

class itemInputForm(forms.Form):
    name = forms.CharField(max_length=50,label = 'Enter item name',required=True)
    weight_lbs = forms.DecimalField(max_digits=6,decimal_places=2, required=True)
    value_in_gold = forms.DecimalField(max_digits=20,decimal_places=2, required=True)
    source = forms.URLField(max_length=20, required=False,label = 'Enter source URL if available')
