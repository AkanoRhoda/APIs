from dataclasses import field
from tkinter import CASCADE
from unicodedata import name
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Link (models.Model):
    target_url = models.URLField(max_length= 200)
    name = models.CharField(max_length= 200)
    identifier = models.SlugField(max_length= 20,  blank=True, unique=True ) 
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date = models.DateTimeField('1/7-5:33pm')
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.target_url