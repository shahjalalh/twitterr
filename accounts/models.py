from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse_lazy

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')

    def __str__(self):
        return str(self.following.all().count())
