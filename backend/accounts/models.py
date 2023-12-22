from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('mechanic', 'Mechanic'),
        ('car_owner', 'Car_Owner'),
    ]

    username = None
    email = models.EmailField(unique=True)
    full_names = models.CharField(max_length=100, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='Customer')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_names', ]

    objects = CustomUserManager()

    def __str__(self):
        return self.full_names
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_no = models.IntegerField(default = 0)
    about = models.TextField(max_length=200, blank=True)
    location = models.CharField(max_length=100)
    is_first_login = models.BooleanField(default=True)

    def __str__(self):
        return self.full_names
