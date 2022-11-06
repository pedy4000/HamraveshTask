from django.db import models
from django.utils import timezone

class App(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    environment = models.CharField(max_length=1028, default='{}')
    command = models.CharField(max_length=1028)
    

class Container(models.Model):
    app_id = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    environment = models.CharField(max_length=1028)
    command = models.CharField(max_length=1028)
    created_at = models.DateTimeField(max_length=256, default=timezone.now())
