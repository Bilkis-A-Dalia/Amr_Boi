from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=200,unique=True)

    def __str__(self) -> str:
        return self.name