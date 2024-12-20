from django.db import models
from django.utils import timezone

#AbstractUser acts as a "template" for creating your own type of user in Django
from django.contrib.auth.models import AbstractUser

# Create your models here.
ROLES = [
    #('CUSTOMER', 'Customer'),
    ('AIR_CONDITIONER', 'Air Conditioner'),
    ('ALL_IN_ONE', 'All in One'),
    ('CARPENTRY', 'Carpentry'),
    ('ELECTRICITY', 'Electricity'),
    ('GARDENING', 'Gardening'),
    ('HOME_MACHINES', 'Home Machines'),
    ('HOUSEKEEPING', 'Housekeeping'),
    ('INTERIOR_DESIGN', 'Interior Design'),
    ('LOCKS', 'Locks'),
    ('PAINTING', 'Painting'),
    ('PLUMBING', 'Plumbing'),
    ('WATER_HEATERS', 'Water Heaters'),
]

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=100, choices=ROLES, default='None')
    dob = models.DateField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    ##string identifier of the class
    def __str__(self):
        return self.email
    
    #in attempt to resolve this error during python manage.py make migrations
    #Reverse accessor for 'User.user_permissions' clashes with reverse accessor for 'User.user_permissions'.
    groups = None
    user_permissions = None