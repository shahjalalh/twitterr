import re

from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

# Create your models here.

from .validators import validate_content

class TweetManager(models.Manager):

    # def retweet(self, user, parent_obj):


class Tweet(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140, validators=[validate_content])
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked')
    reply = models.BooleanField(verbose_name="Is a reply?", default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    class Meta:
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk": self.pk})

    def get_parent(self):
        the_parent = self
        if self.parent:
            the_parent = self.parent
        return the_parent

    def get_children(self):
        parent = self.get_parent()
        qs = Tweet.objects.filter(parent=parent)
        qs_parent = Tweet.objects.filter(pk=parent.pk)

        return (qs | qs_parent)
