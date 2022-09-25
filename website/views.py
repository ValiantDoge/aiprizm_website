from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    clientinfo = ClientInfoCounter.objects.all()
    testimonial = Testimonial.objects.all()
    team = Team.objects.all()
    context = { 'clientinfo': clientinfo, 'nbar': 'home' , 'testimonial': testimonial, 'team': team}
    return render(request, 'website/index.html', context)

def service(request):
    context = {'nbar': 'service'}
    return render(request, 'website/service.html', context)

def about(request):
    context={'nbar': 'about'}
    return render(request, 'website/about.html', context)

def blog(request):
    context={'nbar': 'blog' , 'dropitem': 'blog'}
    return render(request, 'website/blog.html', context)

def detail(request):
    context={'nbar': 'detail' , 'dropitem': 'blog'}
    return render(request, 'website/detail.html', context)

def feature(request):
    context={'nbar': 'feature' , 'dropitem': 'pages'}
    return render(request, 'website/feature.html', context)

def price(request):
    context={'nbar': 'price', 'dropitem': 'pages'}
    return render(request, 'website/price.html', context)

def quote(request):
    context={'nbar': 'quote' , 'dropitem': 'pages'}
    return render(request, 'website/quote.html', context)

def team(request):
    team = Team.objects.all()
    context={'nbar': 'team' , 'dropitem': 'pages', 'team': team}
    return render(request, 'website/team.html', context)

def testimonial(request):
    testimonial = Testimonial.objects.all()
    context={'nbar': 'testimonial' , 'dropitem': 'pages', 'testimonial': testimonial}
    return render(request, 'website/testimonial.html', context)

def contact(request):
    context={'nbar': 'contact'}
    return render(request, 'website/contact.html', context)
