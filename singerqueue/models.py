from django.db import models
from django.contrib.auth import get_user_model


class Singer(models.Model):
    name = models.CharField(max_length=256)
    song_name = models.CharField(max_length=256)

