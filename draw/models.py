from django.db import models

# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()

    def __str__(self):
        return self.name