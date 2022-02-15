from django.db import models
from django.urls import reverse


class Song(models.Model):
    song_name = models.CharField('Название песни', max_length=100)
    text = models.TextField('Текст Песни')
    year = models.DateField('Дата выхода')
    mp3 = models.FileField(upload_to="files/%Y/%m/%d/", blank=True)
    video = models.FileField(upload_to="files/%Y/%m/%d/", blank=True)
    albums = models.ForeignKey('Album', on_delete=models.CASCADE, verbose_name='Альбом')

    def __str__(self):
        return self.song_name

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    def get_absolute_url(self):
        return reverse('song', kwargs={'song_id': self.pk})


class Album(models.Model):
    album_name = models.CharField('Название альбома', max_length=100)

    def __str__(self):
        return self.album_name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def get_absolute_url(self):
        return reverse('album', kwargs={'album_id': self.pk})


class Concert(models.Model):
    date = models.DateTimeField('Дата')
    city = models.CharField('Город', max_length=100)
    price = models.CharField('Цена', max_length=100)
    photo = models.FileField('Фото', upload_to="photos/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Концерт'
        verbose_name_plural = 'Концерты'

    def get_absolute_url(self):
        return reverse('concert', kwargs={'concert_id': self.pk})


class News(models.Model):
    title = models.CharField('Заголовок', max_length=300, blank=True)
    photo = models.FileField('Фото', upload_to="photos/%Y/%m/%d/", blank=True)
    date = models.DateField('Дата')
    description = models.TextField('Описание')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_id': self.pk})


class Quote(models.Model):
    quote = models.TextField('Цитата')
    from_song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='Из песни')

    def __str__(self):
        return self.quote

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

    def get_absolute_url(self):
        return reverse('quote', kwargs={'quote_id': self.pk})