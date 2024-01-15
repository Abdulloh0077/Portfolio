from django.db import models

class portfolioModels(models.Model):
    photo = models.ImageField()
    Url = models.URLField()
    title = models.CharField(max_length=100)
    date = models.DateField()
    about = models.TextField()
