from django.db import models


# Create your models here.

class User(models.Model):

    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(default="", max_length=32)
    nick_name = models.CharField(default="", max_length=255)
    password = models.CharField(default="", max_length=255)
    head_photo = models.ImageField(upload_to="images/head_photo")

    def __str__(self):
        return self.nick_name


class Music(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    owner_id = models.ForeignKey(User, related_name='owner_id', on_delete=models.CASCADE)
    title = models.CharField(default="", max_length=255)
    artist = models.CharField(default="", max_length=255)
    duration = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    source = models.BinaryField(max_length=5242880)
    album = models.CharField(default="", max_length=255)
    album_photo = models.ImageField(upload_to="images/album")

    def __str__(self):
        return self.title

