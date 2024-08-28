from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime
import os

# Create your models here.


class Products(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    price = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)


class Comments(models.Model):
    product = models.ForeignKey(Products,
                                related_name='comments',
                                on_delete=models.DO_NOTHING,
                                null=True)
    comment = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    file = models.FileField(upload_to=filepath, blank=True)
    title = models.CharField(null=True, blank=True, max_length=50)
    dis = models.TextField()
    date = models.DateField(default=timezone.now)
