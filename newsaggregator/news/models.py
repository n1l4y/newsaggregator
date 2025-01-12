from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name.capitalize()
    
class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    
    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name