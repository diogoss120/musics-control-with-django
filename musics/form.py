
from .models import Song
from django.forms import ModelForm

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'duration', 'spotify_published', 'youtube_published', 'artist']