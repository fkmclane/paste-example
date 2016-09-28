from datetime import datetime, timedelta, timezone

from django.db import models

class Paste(models.Model):
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(default='Unnamed', max_length=128)
    language = models.CharField(default='Unknown', max_length=128)
    expires = models.DateTimeField(default=(datetime.now() + timedelta(days=7)))
    code = models.TextField()

    def __str__(self):
        return str(self.id) + ': ' + str(self.name)

    def should_prune(self):
        return datetime.now(timezone.utc) >= self.expires
