import os
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
def get_avatar_file_path(instance, filename):
    return 'avatar/%s/avatar%s' % (instance.username, os.path.splitext(filename)[1])


def get_music_file_path(instance, filename):
    return 'music/%s/%s' % (instance.id, filename)


def get_share_img_file_path(instance, filename):
    return 'img/%s/%s' % (instance.id, filename)


def get_share_video_file_path(instance, filename):
    return 'video/%s/%s' % (instance.id, filename)


def uuid_general():
    return uuid.uuid1().hex


class User(AbstractUser):
    phone_number = models.CharField(default="", max_length=32)
    avatar = models.ImageField(upload_to=get_avatar_file_path, verbose_name="avatar", null=True)
    intro = models.CharField(default="", max_length=255)

    def __str__(self):
        return '{username:%s, email:%s, phone:%s, avatar:%s, intro:%s}' % (self.username, self.email,
                                                                           self.phone_number, self.avatar,
                                                                           self.intro)


class Music(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid_general)
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    data = models.FileField(upload_to=get_music_file_path)
    title = models.CharField(default="", max_length=255)
    author = models.CharField(default="", max_length=255)
    album = models.CharField(default="", max_length=255)
    album_inf = models.CharField(default="", max_length=255)
    album_pic = models.ImageField(upload_to=get_music_file_path)
    total_time = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Share(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid_general)
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    info = models.CharField(default="", max_length=1024)
    img = models.ImageField(upload_to=get_share_img_file_path)
    audio = models.ForeignKey("Music", on_delete=models.CASCADE)
    video = models.FileField(upload_to=get_share_video_file_path)


class Friend(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid_general)
    owner = models.ManyToManyField("User", related_name="owner")
    friends = models.ManyToManyField("User", related_name="friends")
    intimacy = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid_general)
    owner = models.ManyToManyField("User")
    share_id = models.ManyToManyField("Share")
    comment_inf = models.CharField(default="", max_length=1024)


class Favourite(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid_general)
    owner = models.ManyToManyField("User")
    share_id = models.ManyToManyField("Share")
