from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Dish


def my_view(request):
    return JsonResponse({'message':'hello'})

def get_by_id(request,id):
    return JsonResponse({'data':id })

def get_by_id(request,id):
    dish=Dish.objects.filter(pk=id).first()
    # dish=get_object_or_404(Dish,pk=id)
    return render(request,'catalog/dijdeteil.html',
                  {
        'dish':dish,
        
        })

def  hello (request,name:str):
    return HttpResponse(f'<h1> Hello,{name}</h1>')

def get_catalog(request):
    dishes=Dish.objects.all()
    content={
        'dishes':dishes
    }
    return render(request,'catalog/catlist.html')


# Create your views here.
