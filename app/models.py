from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=255,blank=False,null=False)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    gender=models.CharField(max_length=25)
    def __str__(self):
        return self.name