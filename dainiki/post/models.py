import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
categories = (
    ('INT\'L','International'),
    ('PLT','Politics'),
    ('SPT','Sports')
)
class category(models.Model):
    category = models.CharField(max_length=30,choices=categories)
    def __str__(self):
        return self.category
class post(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/')
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.title}"


class front(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='images')
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.title}"
