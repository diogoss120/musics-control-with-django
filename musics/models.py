from django.db import models
import sqlite3

class Artist(models.Model):
    name = models.CharField(max_length=30)
    date_joined = models.DateTimeField()

    def get_songs(self) -> dict:
        conexao = sqlite3.connect('./db.sqlite3')
        cursor = conexao.cursor()
        cursor.execute("select * from musics_song where artist_id = "+str(self.id)+";")

        musics = {}
        for music in cursor.fetchall():
            musics[music[1]] = {
                "id": music[0],
                "title": music[1],
                "duration": music[2],
                "spotify": music[3],
                "youtube": music[4]}

        conexao.close()

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