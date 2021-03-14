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
