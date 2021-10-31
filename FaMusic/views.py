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
        try:
            account = request.POST.get('account')
            password = request.POST.get('password')
            log.debug(f"account = {account}, password = {password}")
            user = User.objects.filter(id=account)[0]
            if password == user.password:
                return HttpResponse("login sucess!")
            else:
                log.debug("password error!")
                return HttpResponse("account or password error!")
        except BaseException:
            log.debug("login except!")
            return HttpResponse("account or password error!")

def reg(request):
    if request.method == 'POST':
        nickname = request.POST.get('nick_name')
        password = request.POST.get('password')

        user_obj = User.objects.create(nick_name=nickname, password=password)
        log.debug(f"register id = {user_obj.id}, username = {user_obj.nickname}, password = {user_obj.password}")
        return HttpResponse(f"id = {user_obj.id}")
    return HttpResponse("register failed!")