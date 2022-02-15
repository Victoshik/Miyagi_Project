from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('songs/', views.songs, name='songs'),
    path('bio/', views.bio, name='bio'),
    path('albums/', views.albums, name='albums'),
    path('quotes/', views.quotes, name='quotes'),
    path('fon/', views.fon, name='fon'),
    path('concerts/', views.concerts, name='concerts'),
    path('news/', views.news, name='news'),
    path('song/<int:song_id>', views.show_song, name='song'),
    path('album/<int:album_id>', views.show_album, name='album'),
]