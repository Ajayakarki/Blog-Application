import email
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='pictures')
    bio = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)


    def __str__(self):
        return self.user.username

    


