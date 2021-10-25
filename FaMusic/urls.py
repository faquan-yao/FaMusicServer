from django.urls import path

import FaMusic.views


urlpatterns = [
    path('hello_world', FaMusic.views.hello_world),
    path('user', FaMusic.views.famusic_user),
    path('login', FaMusic.views.login),
    path('register', FaMusic.views.reg)
]