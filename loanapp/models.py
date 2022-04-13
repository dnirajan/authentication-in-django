from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CreateUser(User):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=10)
    mobile = models.PositiveIntegerField()

