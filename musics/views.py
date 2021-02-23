from django.shortcuts import render, redirect
from datetime import date, datetime
from .models import Artist, Song
from .form import SongForm


def home(request):
    data = {'artists': Artist.objects.all()}

    for artist in data['artists']:
        temp_date = artist.date_joined.strftime("%d/%m/%Y")
        artist.date_joined = temp_date

    return render(request, 'musics/home.html', data)


def musics(request, id):
    data = {}
    artist = Artist.objects.get(pk=id)
    data['artist'] = artist
    data['musics'] = artist.get_songs()
    return render(request, 'musics/musics.html', data)


def new_song(request):
    #com esses parâmetros posso usar o mesmo form para requisições GET e POST
    form = SongForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('url_home')

    return render(request, 'musics/form.html', {'form': form})


def update_song(request, id):
    song = Song.objects.get(pk=id)
    form = SongForm(request.POST or None, instance=song)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('url_home')

    return render(request, 'musics/form.html', {'form': form, 'song': song})

def delete_song(request, id):
    song = Song.objects.get(pk=id)
    song.delete()
    return redirect('url_home')
