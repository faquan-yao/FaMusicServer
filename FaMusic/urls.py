from django.urls import path
from django.views.static import serve

import FaMusic.views
from FaMusicServer.settings import MEDIA_ROOT, BASE_DIR, MEDIA_URL

urlpatterns = [
    path('register', FaMusic.views.register),
    path('login', FaMusic.views.login),
    path('logout', FaMusic.views.logout),
    path('queryMusic', FaMusic.views.queryMusic),
    path('uploadMusic', FaMusic.views.uploadMusic),
    path('getUserProfile', FaMusic.views.getUserProfile),
    path('medias/<path:path>', serve, {'document_root': f"{MEDIA_ROOT}/../{MEDIA_URL}"}),
]
