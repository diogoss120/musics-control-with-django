from django.contrib import admin
from .models import Song, Artist

#para mostrar uma ação no admin defina uma função dentro desse arquivo e adicione dentro 
#do list actions, vá no admin e selecione o artista, clique em GO e no terminal do servidor
#ira ser impresso o print
def funcao_1(modeladmin, request, queryset):
    print('python')

def funcao_2(modeladmin, request, queryset):
    print('django')

class ArtistAdmin(admin.ModelAdmin):
    actions = [funcao_1, funcao_2]

admin.site.register(Song)
admin.site.register(Artist, ArtistAdmin)