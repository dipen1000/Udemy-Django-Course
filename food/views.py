from django.shortcuts import render, redirect
from django.http import HttpResponse

# to load template file without importing render
from django.template import loader
from .models import *
from .forms import *

def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)
    # return HttpResponse(template.render(context, request)) 

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)
    # return HttpResponse("this is item no: %s" % item_id)

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item_form.html', {'form':form})

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item_form.html', {'form':form, 'item':item})

def delete_item(request, id):
    item = Item.objects.get(id=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/delete_item.html', {'item':item})
    
        