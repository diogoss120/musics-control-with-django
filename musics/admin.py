from django.contrib import admin
from .models import Song, Artist
import sqlite3
from openpyxl import load_workbook
from openpyxl import Workbook
from django.http import HttpResponse


class ArtistAdmin(admin.ModelAdmin):
    def export_musics_from_artist(self, request, queryset):
        conn = sqlite3.connect('./db.sqlite3')
        cursor = conn.cursor()

        print('hello')

        musics = cursor.execute(
            "select s.title, s.duration, s.spotify_published, s.youtube_published from musics_song s join musics_artist a on a.id = s.artist_id where a.id = 2;"
        ).fetchall()
        qtd_musicas = len(musics)
        print('quantidade de músicas: ', str(qtd_musicas))

        #name_artist = cursor.execute()

        caminho = './musics/excel/music.xlsx'
        wb = load_workbook(caminho)
        sheet = wb.active

        sheet['B4'] = "TITLE"
        sheet['C4'] = "DURATION"
        sheet['D4'] = "NO SPOTIFY"
        sheet['E4'] = "NO YOUTUBE"

        colls = ['B', 'C', 'D', 'E']
        coll = 0
        row = 5

        for music in musics:
            print('qtd info da musica -', len(music))

            for caracteristica in music:
                if caracteristica == 1:
                    caracteristica = "Sim"
                elif caracteristica == 0:
                    caracteristica = "Não"
                print(caracteristica, end=' - ')
                sheet[str(colls[coll] + str(row))] = caracteristica
                coll += 1

            coll = 0
            row += 1

        wb.save(caminho)

        conn.close()

        response = HttpResponse(sheet)
        response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        response['Content-Disposition'] = 'attachment; filename=artist_music.xls'

        return response

    actions = [export_musics_from_artist]


admin.site.register(Song)
admin.site.register(Artist, ArtistAdmin)