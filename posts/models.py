from django.db import models
from datetime import datetime
# Create your models here.


class post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    created_at=models.DateField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    message=models.TextField()
    created_at=models.DateField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title    