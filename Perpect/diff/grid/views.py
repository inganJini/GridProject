from django.shortcuts import render, redirect, get_object_or_404
from .models import KeyModel, MasterModel, DetailModel
from django.contrib.auth.decorators import login_required

# Create your views here.
def grid(request):
    for_index = range(8)
    return render(request, 'grid.html',{'for_index':for_index})

def mygrid(request, username):
    #for_index = range(8)
    #return render(request, 'mygrid.html',{'for_index':for_index})
    my_key = KeyModel.objects.filter(username=username)
    master_value = MasterModel.objects.all()
    context_key = {'my_key':my_key,'master_value':master_value}

    return render(request, 'mygrid.html', context_key)

def detail(request, title):

    my_master = MasterModel.objects.filter(title=key)
    detail_value = DetailModel.objects.all()
    context_key = {'my_master':my_master , 'detail_value':detail_value}

    return render(request, 'detail.html', context_key)

def create(request):
    return render(request, 'create.html')