import logging

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from django.shortcuts import render

from FaMusicServer.settings import MEDIA_URL
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
        avatar = request.FILES.get("avatar")

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
            return HttpResponse(user.toJson())
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
        log.debug(f"user = {request.user.username}")
        musics = request.user.music_set.all()
        if musics is not None:
            log.debug(f"music.count() = {musics.count()}")
            return HttpResponse(musics.first())
        else:
            return HttpResponse("queryMusic error1.")
    return HttpResponse("queryMusic error2.")


@login_required
def uploadMusic(request):
    if request.method == "POST":
        log.debug(f"user = {request.user.username}")
        owner = request.user
        data = request.FILES.get("data")
        title = request.POST.get("title")
        author = request.POST.get("author")
        album = request.POST.get("album")
        album_inf = request.POST.get("album_inf")
        album_pic = request.FILES.get("album_pic")
        total_time = request.POST.get("time")
        m = request.user.music_set.all().first()
        if m is None:
            music = Music.objects.create(owner=owner, title=title, author=author,
                                         album=album, album_inf=album_inf,
                                         total_time=total_time)
            music.data = data
            music.album_pic = album_pic
            music.save()
            return HttpResponse(music)
        else:
            return HttpResponse(f"music {title} has been upload.")

    return HttpResponse("Upload music error.")


def getUserProfile(request):
    user = User.objects.all().get(username="faquan.yao")
    return render(request, "FaMusic/userprofile.html", {
        "user": user,
        "MEDIA_URL": MEDIA_URL
    })
