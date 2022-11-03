from django.db import  models

# Create model here:-

class Employee(models.Model):
    f_name=models.CharField(max_length=100)
    l_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    email=models.EmailField()

