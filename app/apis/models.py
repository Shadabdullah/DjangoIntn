from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField('Work', related_name='artists')

    def __str__(self):
        return self.name



class Work(models.Model):
    WORK_TYPES = (
        ('youtube', 'YouTube'),
        ('instagram', 'Instagram'),
        ('other', 'Other'),
    )
    link = models.URLField()
    work_type = models.CharField(max_length=10, choices=WORK_TYPES)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.link
