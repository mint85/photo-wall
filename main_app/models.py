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