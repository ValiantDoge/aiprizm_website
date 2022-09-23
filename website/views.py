from unicodedata import name
from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'website/index.html')

def service(request):
    return render(request, 'website/service.html')

def about(request):
    return render(request, 'website/about.html')

def blog(request):
    return render(request, 'website/blog.html')

def contact(request):
    return render(request, 'website/contact.html')

def detail(request):
    return render(request, 'website/detail.html')

def feature(request):
    return render(request, 'website/feature.html')

def price(request):
    return render(request, 'website/price.html')

def quote(request):
    return render(request, 'website/quote.html')

def team(request):
    return render(request, 'website/team.html')

def testimonial(request):
    return render(request, 'website/testimonial.html')