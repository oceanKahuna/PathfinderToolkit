from django.http import HttpResponse
from django.shortcuts import render
from inventory.forms import itemInputForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

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