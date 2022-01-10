import logging
import json

from django.http import HttpResponse
from django.http import JsonResponse

from .models import User

log = logging.getLogger(__name__)


# Create your views here.

def register(request):
    if request.method == 'POST':
        phone = request.POST.get('phone_number')
        nickname = request.POST.get('nick_name')
        password = request.POST.get('password')
        photo = request.FILES.get("head_photo")
        try:
            user = User.objects.get(nick_name=nickname)
            log.debug(f"nick_name {user.nick_name} has registered.")
            return HttpResponse(f"register failed, nick_name has registered.")
        except User.DoesNotExist:
            user_obj = User.objects.create(phone_number=phone, nick_name=nickname, password=password)
            log.debug(f"register id = {user_obj.id}, username = {user_obj.nick_name}, password = {user_obj.password}")
            user_obj.head_photo = photo
            user_obj.save()
            return HttpResponse(f"id = {user_obj.id}")

    return HttpResponse("register failed!")


def login(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        log.debug(f"account = {account}, password = {password}")
        try:
            user = User.objects.get(id=account)
            if password == user.password:
                return HttpResponse(user)
            else:
                log.debug("password error!")
                return HttpResponse("account or password error!")
        except User.DoesNotExist:
            log.debug("account is not exist!")
            return HttpResponse("account is not exist!")
    else:
        return HttpResponse("request error!")


def unregister(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        log.debug(f"unregister account {account}")
        try:
            user = User.objects.get(id=account)
            user.delete()
            return HttpResponse("unregister success!")
        except User.DoesNotExist:
            log.debug(f"account {account} not exist.")
            return HttpResponse("unregister error")
    else:
        return HttpResponse("unregister error")


def queryMusic(request):
    pass


def uploadMusic(request):
    pass
