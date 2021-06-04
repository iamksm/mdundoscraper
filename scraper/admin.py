from django.contrib import admin

from .models import ArtistQuery, ArtistContent

admin.site.register(ArtistQuery)
admin.site.register(ArtistContent)
