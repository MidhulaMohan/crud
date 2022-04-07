from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    class meta:
        db_table="Employ"