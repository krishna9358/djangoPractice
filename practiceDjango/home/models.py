from django.db import models

# Create your models here.
class notes(models.Model):
    title = models.CharField(max_length= 100)
    text  = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class notes2(models.Model):
    title = models.CharField(max_length= 100)
    text  = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
