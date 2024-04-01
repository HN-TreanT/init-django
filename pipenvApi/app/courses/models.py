from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    avartar = models.ImageField(upload_to="upload/%Y/%m")
class Category(models.Model): #courses_category
    name = models.CharField(null=False, unique=True, max_length=250 )
    description = models.TextField()
    date = models.DateField(default=now)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    subject = models.TextField(null=False)
    description = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    
    def __str__(self):
        return self.subject
