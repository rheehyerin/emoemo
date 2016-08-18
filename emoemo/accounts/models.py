from django.conf import settings
from django.db import models

class Follow(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="who_follows")
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="who_is_followed")
    follow_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.follow_time)

