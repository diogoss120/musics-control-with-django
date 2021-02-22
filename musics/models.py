from django.db import models
import sqlite3


class Artist(models.Model):
    name = models.CharField(max_length=30)
    date_joined = models.DateTimeField()

    def get_songs(self):
        conexao = sqlite3.connect('./db.sqlite3')
        cursor = conexao.cursor()
        cursor.execute("select * from musics_song where artist_id = "+str(self.id)+";")

        musicas = {}
        for music in cursor.fetchall():
            musicas[music[1]] = {
                "id": music[0],
                "title": music[1],
                "duration": music[2],
                "spotify": music[3],
                "youtube": music[4]}

        conexao.close()

        return musicas

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Artists'


class Song(models.Model):
    title = models.CharField(max_length=30)
    duration = models.IntegerField()
    spotify_published = models.BooleanField()
    youtube_published = models.BooleanField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Songs'