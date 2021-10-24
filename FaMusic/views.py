from django.shortcuts import render
from django.http import HttpResponse
from .models import User


# Create your views here.

def hello_world(request):
    return HttpResponse("Hello world")

def famusic_user(request):
    user = User.objects.all()[0]
    nick_name = user.nick_name
    return HttpResponse(nick_name)
