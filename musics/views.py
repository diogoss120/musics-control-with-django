from django.shortcuts import render, redirect
from datetime import date, datetime
from .models import Artist, Song
from .form import SongForm


def get_artist() -> Artist:
    # recuperando todos os artistas em ordem alfabetica
    artists = Artist.objects.order_by('name')
    for artist in artists:
        temp_date = artist.date_joined.strftime("%d/%m/%Y")
        artist.date_joined = temp_date
    return artists

def home(request) -> render:  

    # dictionary que será enviado para o template django
    data = {'artists': get_artist()}

    return render(request, 'musics/home.html', data)


def musics(request, id: int) -> render:
    # dictionary que será enviado para o template django
    data = {}

    # recuperando o artista cujo id foi passado como parâmetro na request
    artist = Artist.objects.get(pk=id)

    data['artist'] = artist
    data['musics'] = artist.get_songs()
    data['artists'] = get_artist()

    return render(request, 'musics/musics.html', data)


def new_song(request) -> render or redirect:

    # recuperando um formulário existente em caso de update ou criando um novo
    form = SongForm(request.POST or None)

    # identificando se é uma música existente e salvando caso ela seja válida
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('url_home')

    # dictionary que será enviado para o template django
    data = {}
    data['form'] = form
    data['message'] = 'New Music'
    data['artists'] = get_artist()

    return render(request, 'musics/form.html', data)


def update_song(request, id: int) -> render or redirect:
    # recuperando música que será editada
    song = Song.objects.get(pk=id)
    form = SongForm(request.POST or None, instance=song)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('url_new_song')

    # dictionary que será enviado para o template django
    data = {}
    data['form'] = form
    data['message'] = 'Edit Music'
    data['artists'] = get_artist()
    data['song'] = song

    return render(request, 'musics/form.html', data)


def delete_song(request, id: int) -> redirect:
    # recuperando e deletando a música desejada
    song = Song.objects.get(pk=id)
    song.delete()
    return redirect('url_home')
