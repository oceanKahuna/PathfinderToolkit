from django.http import HttpResponse
from django.shortcuts import render
from inventory.forms import itemInputForm

# Create your views here.
def index(request): 
    return HttpResponse("Hello, world. This is the index view of the Inventory App.") 

def item_form_view(request):
    form = itemInputForm()
    context = {'form':form}
    return render(request, 'item.html',context )