from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    joined_date = models.DateTimeField('date joined')
    def __str__(self):
        return self.username
    
class Game(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=5000)
    link = models.CharField(max_length=255)
    date_published = models.DateTimeField('date published')
    created_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title