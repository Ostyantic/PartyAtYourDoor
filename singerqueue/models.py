from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Singer(models.Model):
    name = models.CharField(max_length=256)
    song_name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
