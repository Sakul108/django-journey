from django.shortcuts import render
from .models import ProductItem

def product(request):
    product=ProductItem.objects.all()
    return render(request,'product/index.html',{'products':product})
# Create your views here.
