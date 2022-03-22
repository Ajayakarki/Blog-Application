from tkinter import CASCADE
from typing import cast
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='posts')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    

class Comment(models.Model):
    cmt_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    cmt_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=5000)

    # def get_absolute_url(self):
    #     return reverse('blog-detail', kwargs={'pk': self.pk})
    
