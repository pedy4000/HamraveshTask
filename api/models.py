from django.db import models

class App(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    envs = models.CharField(max_length=256)
    command = models.CharField(max_length=256)