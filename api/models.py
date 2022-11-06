from django.db import models

class App(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    environment = models.CharField(max_length=256, default='{}')
    command = models.CharField(max_length=256)