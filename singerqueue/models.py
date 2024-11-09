from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Singer(models.Model):
    name = models.CharField(max_length=256)
    song_name = models.CharField(max_length=256)
    song_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class ContactInfo(models.Model):
    social_type_choices = [
        ('', 'Please pick a social contact type'),
        ('tiktok', 'TikTok'),
        ('X', 'X'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('phone_number', 'Phone Number'),
        ('email', 'Email'),


    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)
    social_types = models.CharField(max_length=12, choices=social_type_choices, default='')
    social_contact = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('queue')
