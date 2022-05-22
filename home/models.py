from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    joined_date = models.DateTimeField('date joined')
    def __str__(self):
        return self.username