
from django.db import models

# Create your models here.
class Products(models.Model):
    title= models.CharField(max_length=100)
    describtion = models.CharField(max_length=222)
    quantity = models.IntegerField(null=True,blank=True)
    size = models.CharField(max_length=222)
    grade = models.CharField(max_length=222)
    QUALITY = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    )
    quality = models.CharField(max_length=1, choices=QUALITY)
    COLOURS = (
        ('Gr', 'Grey'),
        ('Bu', 'Blue'),
        ('Bl', 'Black'),
    )
    colours = models.CharField(max_length=2, choices=COLOURS)
    
    def __str__(self):
        return self.title