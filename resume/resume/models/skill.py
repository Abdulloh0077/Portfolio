from django.db import models


class SkillModels(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title