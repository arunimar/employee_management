from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    employee_id = models.CharField(max_length=24)
    phone = models.CharField(max_length=16)
    address = models.TextField(null=True)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)
    gender = models.IntegerField(choices=((1, 'Female'), (2, 'Male'), (3, 'Others')), default=1)
