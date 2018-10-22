import re

from django.conf import settings
from django.urls import reverse
from django.db import models

# Create your models here.


class Tweet(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140)
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked')
    reply = models.BooleanField(verbose_name="Is a reply?", default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)
