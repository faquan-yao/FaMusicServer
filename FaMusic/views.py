import logging

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import User
from .models import Music

log = logging.getLogger(__name__)


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        intro = request.POST.get("intro")
        avatar = request.POST.get("avatar")

        try:
            user = User.objects.get(username=username)
            log.debug(f"nick_name {user.username} has registered.")
            return HttpResponse(f"register failed, nick_name has registered.")
        except User.DoesNotExist:
            user_obj = User.objects.create_user(username=username, password=password,
                                                phone_number=phone_number, email=email,
                                                intro=intro, avatar=avatar)
            user_obj.avatar = avatar
            user_obj.save()

            log.debug(f"register username = {user_obj.username}")
            return HttpResponse(f"username = {user_obj.username}")

    return HttpResponse("register failed!")


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        log.debug(f"username = {username}, password = {password}")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponse("login successful")
        else:
            return HttpResponse("login error!")
    else:
        return HttpResponse("login error!")


def logout(request):
    auth.logout(request)
    return HttpResponse("logout successful")


@login_required
def queryMusic(request):
    if request.method == "POST":
        musics = Music.objects.filter(owner__music=request.user.pk)
        if musics is not None:
            print(musics.count())
            return HttpResponse(musics.count())
        else:
            return HttpResponse("queryMusic error1.")
    return HttpResponse("queryMusic error2.")




@login_required
def uploadMusic(request):
    pass
