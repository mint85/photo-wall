from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Photo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('photo_detail', kwargs={'photo_id': self.id})

class PhotoFile(models.Model):
    url = models.CharField(max_length=200)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for photo_id: {self.photo_id} @{self.url}"