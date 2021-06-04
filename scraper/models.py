from django.db import models


class ArtistQuery(models.Model):
    artist_name = models.CharField(max_length=20)

    def __str__(self):
        return self.artist_name


class ArtistContent(models.Model):
    artist = models.ForeignKey(ArtistQuery, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=50)
    genre = models.CharField
    duration = models.DurationField

    def __str__(self):
        return self.song_name
