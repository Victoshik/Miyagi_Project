from django.contrib import admin


from .models import *

admin.site.register(Song)
admin.site.register(Album)
admin.site.register(News)
admin.site.register(Concert)
admin.site.register(Quote)