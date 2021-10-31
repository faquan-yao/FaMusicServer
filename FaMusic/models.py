from django.db import models


# Create your models here.

class User(models.Model):

    id = models.AutoField(primary_key=True)
    phone_number = models.TextField(default="")
    nick_name = models.TextField(default="")
    password = models.TextField(default="")
    head_photo = models.CharField(max_length=65536)

    def __str__(self):
        return self.nick_name


class Music(models.Model):
    id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(User, related_name='owner_id', on_delete=models.CASCADE)
    title = models.TextField(default="")
    artist = models.TextField(default="")
    duration = models.TextField(default="0")
    size = models.TextField(default="0")
    source = models.CharField(max_length=5242880)
    album = models.TextField(default="")
    album_photo = models.CharField(max_length=65536)

    def __str__(self):
        return self.title

