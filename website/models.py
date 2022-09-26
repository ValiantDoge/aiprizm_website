from distutils.command.upload import upload
import email
from email import message
from email.policy import default
from http import client
from django.db import models

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=50)
    service_desc = models.CharField(max_length=5000)
    service_icon = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.service_name

class ClientInfoCounter(models.Model):
    info_heading = models.CharField(max_length=50)
    info_count = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.info_heading

class Client(models.Model):
    client_name= models.CharField(max_length=50)
    client_logo= models.ImageField(upload_to="website/images", default="")

    def __str__(self):
        return self.client_name

class Testimonial(models.Model):
    testclient_pic=models.ImageField(upload_to="website/images", default="")
    testclient_name=models.CharField(max_length=50)
    testclient_profession=models.CharField(max_length=50)
    testclient_desc=models.CharField(max_length=500)

    def __str__(self):
            return self.testclient_name

class Team(models.Model):
    team_member_pic=models.ImageField(upload_to="website/images", default="", blank=True)
    team_member_name=models.CharField(max_length=50)
    team_member_desc=models.CharField(max_length=1000)
    team_member_profession=models.CharField(max_length=50, default='')
    team_member_twitter=models.URLField(max_length=300, default='', blank=True)
    team_member_facebook=models.URLField(max_length=300, default='', blank=True)
    team_member_instagram=models.URLField(max_length=300, default='', blank=True)
    team_member_stackoverflow=models.URLField(max_length=300, default='', blank=True)
    team_member_linkedin=models.URLField(max_length=300, default='', blank=True)

    def __str__(self):
            return self.team_member_name

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.email


