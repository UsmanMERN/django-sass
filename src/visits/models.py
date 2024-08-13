from django.db import models

# Create your models here.


class PageVists(models.Model):
    path = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
