from django.db import models

# Create your models here.
class Employee(models.Model):
    uname = models.CharField(max_length=50)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    class Meta:
        db_table = 'employee'
