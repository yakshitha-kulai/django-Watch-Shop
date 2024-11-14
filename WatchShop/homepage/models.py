from django.db import models

# Create your models here.
# Watches Table created
class Watches(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.FloatField()

    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

class WatchesUploads(models.Model):
    name = models.CharField(max_length = 100) 
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='watches_images/')

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
