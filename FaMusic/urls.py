from django.urls import path

import FaMusic.views


urlpatterns = [
    path('register', FaMusic.views.register),
    path('login', FaMusic.views.login),
    path('logout', FaMusic.views.logout),
    path('queryMusic', FaMusic.views.queryMusic),
    path('uploadMusic', FaMusic.views.uploadMusic)
]