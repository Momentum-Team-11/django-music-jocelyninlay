from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=225)
    artist = models.CharField(max_length=225)
    date_created = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)

def __str__(self):
    return self.title