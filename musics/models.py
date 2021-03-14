from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=30)
    date_joined = models.DateTimeField()

    def get_songs(self) -> dict:

        # recuperando as músicas do artista
        get_data_musics = Song.objects.filter(artist=self.id)
        
        # passando todas as músicas para um dictionary
        musics = {}
        for music in get_data_musics:
            musics[music.title] = {
                "id": music.id,
                "title": music.title,
                "duration": music.duration,
                "spotify": music.spotify_published,
                "youtube": music.youtube_published}

        return musics

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Artists'


class Song(models.Model):
    title = models.CharField(max_length=30)
    duration = models.IntegerField()
    spotify_published = models.BooleanField()
    youtube_published = models.BooleanField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Songs'