from django.conf import settings
from django.db import models

class Follow(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="who_follows")
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="who_is_followed")
    is_approved = models.BooleanField(default=False)
    request_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.is_approved)