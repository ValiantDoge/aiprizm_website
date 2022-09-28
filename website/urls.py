from django.urls import path
from website import views

urlpatterns = [
    path('',  views.index, name='index'),
    path('about/',  views.about, name='about'),
    path('blog/',  views.blog, name='blog'),
    path('contact/',  views.contact, name='contact'),
    path('detail/',  views.detail, name='detail'),
    path('feature/',  views.feature, name='feature'),
    path('quote/',  views.quote, name='quote'),
    path('service/',  views.service, name='service'),
    path('team/',  views.team, name='team'),
    path('testimonial/',  views.testimonial, name='testimonial'),
]