from django.db import models

# Create your models here.
class Student(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=50)
    rollno = models.IntegerField()
    place = models.CharField(max_length=50)
    phone = models.IntegerField()