from django.http import HttpResponse
from django.shortcuts import render
# Import your ProductItem model from the product app
from product.models import ProductItem

def home(request):
    # Query all uploaded products/images from the database
    products = ProductItem.objects.all()
    # Pass 'products' to your index.html template
    return render(request, 'website/index.html', {'products': products})


def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')


def team(request):
    return render(request, 'website/team.html')


def services(request):
    return render(request, 'website/services.html')

def doctors(request):
       return render(request, 'doctors.html')


# from django.http import HttpResponse
# from django.shortcuts import render

# def home(request):
#     return render(request,'website/index.html')



# def about(request):
#     return render(request,'website/about.html')

# def contact(request):
#     return render(request,'website/contact.html')


# def team(request):
#     return render(request,'website/team.html')


# def services(request):
#     return render(request,'website/services.html')
