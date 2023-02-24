from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField('Work')


class Work(models.Model):
    YOUTUBE = 'YT'
    INSTAGRAM = 'IT'
    OTHER = 'OT'
    WORK_TYPE_CHOICES = [
        (YOUTUBE, 'Youtube'),
        (INSTAGRAM, 'Instagram'),
        (OTHER, 'Other'),
    ]
    link = models.URLField()
    work_type = models.CharField(choices=WORK_TYPE_CHOICES, max_length=2)


@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)
