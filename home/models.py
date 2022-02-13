from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    # passsword=models.CharField(max_length=20)
    address=models.TextField()
    
    def __str__(self):
        return self.name