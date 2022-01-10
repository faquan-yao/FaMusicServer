import os

from django.db import models


# Create your models here.
def get_file_path(instance, filename):
    return 'images/users/%s/%s_head_photo%s' % (instance.id, instance.id, os.path.splitext(filename)[1])


class User(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(default="", max_length=32)
    nick_name = models.CharField(default="", max_length=255)
    password = models.CharField(default="", max_length=255)
    head_photo = models.ImageField(upload_to=get_file_path, verbose_name="head", null=True)

    def __str__(self):
        return '{id:%s, phone_number:%s, nick_name:%s, password:%s, head_photo:%s}' % (self.id, self.phone_number,
                                                                                       self.nick_name, self.password,
                                                                                       self.head_photo)


class Music(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    owner_id = models.ForeignKey(User, related_name='owner_id', on_delete=models.CASCADE)
    title = models.CharField(default="", max_length=255)
    artist = models.CharField(default="", max_length=255)
    duration = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    source = models.BinaryField(max_length=5242880)
    album = models.CharField(default="", max_length=255)
    album_photo = models.ImageField(upload_to=f"images/album")

    def __str__(self):
        return self.title
