from django.urls import path

import FaMusic.views


urlpatterns = [
    path('register', FaMusic.views.register),
    path('login', FaMusic.views.login),
    path('unregister', FaMusic.views.unregister)
]