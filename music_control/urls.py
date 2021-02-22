"""music_control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from musics.views import home, musics, new_song, update_song, delete_song

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('musics/<int:id>', musics, name='url_musics'),
    path('new/', new_song, name='url_new_song'),
    path('update/<int:id>', update_song, name='url_update_song'),
    path('delete/<int:id>', delete_song, name='url_delete_song'),
]
