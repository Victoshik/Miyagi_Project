from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *

menu = [{'title': 'Биография', 'url': 'bio'},
        {'title': 'Новости', 'url': 'news'},
        {'title': 'Песни', 'url': 'songs'},
        {'title': 'Альбомы', 'url': 'albums'},
        {'title': 'Концерты', 'url': 'concerts'},
        {'title': 'Обои', 'url': 'fon'},
        {'title': 'Цитаты', 'url': 'quotes'},
        ]


def index(request):
    concert = Concert.objects.all()
    dict = {'menu': menu, 'title': 'Home', 'concert': concert}
    return render(request, 'miyagi_app/index.html', dict)


def about(request):
    elem = {'menu': menu, 'title': 'About'}
    return render(request, 'miyagi_app/about.html', elem)


def bio(request):
    elem = {'menu': menu, 'title': 'Биография'}
    return render(request, 'miyagi_app/bio.html', elem)


def news(request):
    elem = {'menu': menu, 'title': 'Новости'}
    return render(request, 'miyagi_app/news.html', elem)


def songs(request):
    song = Song.objects.all()
    elem = {'menu': menu, 'title': 'Песни', 'songs': song}
    return render(request, 'miyagi_app/songs.html', elem)


def show_song(request, song_id):
    song = Song.objects.get(pk=song_id)
    elem = {'menu': menu, 'title': 'Песня', 'songs': song}
    return render(request, 'miyagi_app/show_song.html', elem)


def albums(request):
    album = Album.objects.all()
    elem = {'menu': menu, 'title': 'Альбомы', 'album': album}
    return render(request, 'miyagi_app/albums.html', elem)


def show_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    elem = {'menu': menu, 'title': 'Альбомы', 'album': album, 'al_selected': 0}
    return render(request, 'miyagi_app/show_album.html', elem)


def concerts(request):
    elem = {'menu': menu, 'title': 'Концерты'}
    return render(request, 'miyagi_app/concerts.html', elem)


def fon(request):
    elem = {'menu': menu, 'title': 'Обои'}
    return render(request, 'miyagi_app/fon.html', elem)


def quotes(request):
    elem = {'menu': menu, 'title': 'Цитаты'}
    return render(request, 'miyagi_app/quotes.html', elem)