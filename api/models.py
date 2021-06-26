from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils import tree



class IpAddress(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Post')
    description = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    views = models.ManyToManyField(IpAddress, blank=True)

    def __str__(self):
        return self.name
