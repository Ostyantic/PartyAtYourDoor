from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    room_id = models.CharField(default='000000', max_length=6)
    intermission = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.username
