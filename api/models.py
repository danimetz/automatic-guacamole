from django.db import models

# Create your models here.

class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    spotify_id = models.CharField(max_length=50)
    uri = models.CharField(max_length = 100)

def __str__(self):
    return '%s - %s' % (self.title, self.artitst)

class User(models.Model):
    spotify_id = models.CharField(max_length=50)
    playlist_id = models.CharField(max_length=50)
    access_key = models.CharField(max_length=50)

def __str__(self):
    return self.spotify
