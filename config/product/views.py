from django.shortcuts import render,get_object_or_404
from .models import ProductItem, Department

def product(request):
    product=ProductItem.objects.all()
    return render(request,'product/index.html',{'products':product})
# Create your views here.


def review(request,pk):
    product=get_object_or_404(ProductItem,pk=pk)
    context={
        'product':product,
        'reviews':product.reviews.all()
    }
    return render(request,'product/review.html',context)


def certificate(request,pk):
    product=get_object_or_404(ProductItem,pk=pk)
    context={
        'product':product,
        'certificate':product.certificate
    }
    return render(request,'product/certificate.html',context)


def details(request,pk):
    product=get_object_or_404(ProductItem,pk=pk)
    context={
        'product':product,
        'reviews':product.reviews.all()
    }
    return render(request,'product/details.html',context)


def departments(request):
    departments = Department.objects.all()
    return render(request, 'product/departments.html', {'departments': departments})


def department_detail(request, slug):
    department = get_object_or_404(Department, slug=slug)
    return render(request, 'product/department_detail.html', {'department': department})