from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def my_view(request):
    return JsonResponse({'message':'hello'})

def get_by_id(request,id):
    return JsonResponse({'data':id })

def  hello (request,name:str):
    return HttpResponse(f'<h1> Hello,{name}</h1>')

def get_catalog(request):
    return render(request,'catalog/catlist.html')

# Create your views here.
