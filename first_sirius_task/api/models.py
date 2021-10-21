from django.db import models


class Link(models.Model):
    redirectTo = models.CharField(max_length=200, default='')
    urlToShorten = models.CharField(max_length=200, default='')
    token = models.CharField(max_length=200, default='')
    viewCount = models.IntegerField(default=0)
