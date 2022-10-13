from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()

    # Create your models here.
    def __str__(self):
        return self.name
