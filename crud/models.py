from django.db import models

# Create your models here.
class employees(models.Model):
    ename=models.CharField(max_length=100)
    eemail=models.CharField(max_length=100)
    eaddress=models.CharField(max_length=100)
    ephone=models.CharField(max_length=100)
