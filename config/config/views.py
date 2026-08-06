from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'website/index.html')


def about(request):
    return render(request,'website/about.html')

def contact(request):
    return render(request,'website/contact.html')


def team(request):
    return render(request,'website/team.html')


def services(request):
    return render(request,'website/services.html')
