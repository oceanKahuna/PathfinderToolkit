from django.http import HttpResponse
from django.shortcuts import render
from inventory.forms import itemInputForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .models import Item
# Create your views here.

def index(request): 
    if request.user.is_anonymous():
        raise PermissionDenied()
    return HttpResponse("Hello, world. This is the index view of the Inventory App.") 

@login_required
def item_form_view(request):
    permission_required='inventory.add_item'
    form = itemInputForm()
    if request.method=='POST':
        form = itemInputForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'item.html',context )

def about(request):
    about_content={'about':'This is a project to supplement functionality on role20 by making inventory, spell management, and leveling easier'}
    return render(request, 'about.html',about_content)

def all_items(request):
    items = Item.objects.all()
    items_dict = {'items': items}
    return render(request, 'all_items.html',items_dict)

def home(request): 
    return render(request, "home.html", {}) 

def register(request): 
    return render(request, "register.html", {}) 

def login(request): 
    return render(request, "login.html", {}) 
    