from django.shortcuts import render, redirect
from datetime import date, datetime
from .models import Artist, Song
from .form import SongForm


def get_artist() -> Artist:
    #artists = Artist.objects.all()
    artists = Artist.objects.order_by('name')
    for artist in artists:
        temp_date = artist.date_joined.strftime("%d/%m/%Y")
        artist.date_joined = temp_date
    return artists


def home(request) -> render:
    data = {'artists': get_artist()}

    return render(request, 'musics/home.html', data)


def musics(request, id: int) -> render:
    data = {}
    artist = Artist.objects.get(pk=id)
    data['artist'] = artist
    data['musics'] = artist.get_songs()
    data['artists'] = get_artist()
    return render(request, 'musics/musics.html', data)


def new_song(request) -> render or redirect:
    form = SongForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('url_home')

    data = {}
    data['form'] = form
    data['message'] = 'New Music'
    data['artists'] = get_artist()

    return render(request, 'musics/form.html', data)


def update_song(request, id: int) -> render or redirect:
    song = Song.objects.get(pk=id)
    form = SongForm(request.POST or None, instance=song)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('url_new_song')

    data = {}
    data['form'] = form
    data['message'] = 'Edit Music'
    data['artists'] = get_artist()
    data['song'] = song

    return render(request, 'musics/form.html', data)


def delete_song(request, id: int) -> redirect:
    song = Song.objects.get(pk=id)
    song.delete()
    return redirect('url_home')
