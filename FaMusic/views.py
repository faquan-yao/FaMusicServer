from django.shortcuts import render
from django.http import HttpResponse
from .models import User
import logging

log = logging.getLogger(__name__)

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello FaMusic")

def famusic_user(request):
    user = User.objects.all()[0]
    nick_name = user.nick_name
    return HttpResponse(nick_name)

def login(request):
    if request.method == 'POST':
        account = request.POST.get('Account')
        password = request.POST.get('Password')
        log.debug(f"Account = {account}, password = {password}")
        user = User.objects.filter(id=account)[0]
        if password == user.password:
            return HttpResponse("login sucess!")
        else:
            return HttpResponse("Account or password error!")

def reg(request):
    if request.method == 'POST':
        username = request.POST.get('login_name')
        password = request.POST.get('password')

        user_obj = User.objects.create(login_name=username, password=password)
        log.debug(f"register username = {user_obj.login_name}, password = {user_obj.password}")
        return HttpResponse("register success!")
    return HttpResponse("register failed!")