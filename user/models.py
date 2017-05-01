from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()

    # password = models.CharField(max_length=30)
    # an object for cart for the user is needed here, to be added to base.html cart field

    def __str__(self):
        return self.email.__str__()


class Area(models.Model):
    # thana actually
    name = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    postal_code = models.PositiveIntegerField()

    def __str__(self):
        return self.name.__str__()