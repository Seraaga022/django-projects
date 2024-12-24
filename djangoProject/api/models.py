from django.db import models

class model(models.Model):
    name = models.CharField
    language = models.CharField
    price = models.CharField(max_length=10)