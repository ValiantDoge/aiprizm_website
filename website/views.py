from http.client import HTTPResponse
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from website.forms import ContactForm
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

def quote(request):
    context={'nbar': 'quote' , 'dropitem': 'pages'}
    return render(request, 'website/quote.html', context)

def team(request):
    team = Team.objects.all().order_by('order')
    context={'nbar': 'team' , 'dropitem': 'pages', 'team': team}
    return render(request, 'website/team.html', context)

def testimonial(request):
    testimonial = Testimonial.objects.all()
    context={'nbar': 'testimonial' , 'dropitem': 'pages', 'testimonial': testimonial}
    return render(request, 'website/testimonial.html', context)

def contact(request):
    form  = ContactForm()

    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        if form.is_valid():
            
            body = {
                'name': form.cleaned_data['name'],
                'subject': form.cleaned_data['subject'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            # message = "\n".join(body.values())

            #Email to User
            subject = "Received Inquiry"
            message = f"Hi {body.get('name')}, we have received your email. We'll get back to you shortly."
            email = body.get('email')

            #Email to Comapny
            subject_company = f"(Website Inquiry) "+body.get('subject')
            message_company = body.get('message')
            email_company = 'agnelofernandes475@gmail.com'
            form.save()

            try:
                #Email to User
                send_mail(subject, message, 'settings.EMAIL_HOST_USER',[email])

                #Email to Company
                send_mail(subject_company, message_company, 'settings.EMAIL_HOST_USER',[email_company])
            except BadHeaderError:
                return HTTPResponse('Invalid header found.')
            # return HttpResponse("Your query has been sent.", status=200)

    context={'nbar': 'contact', 'form': form}
    return render(request, 'website/contact.html', context)


