from django.db import models
from django.utils import timezone

from main.models import User

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Company, Customer

CHOICES = (
        ('Air Conditioner', 'Air Conditioner'),
        ('Carpentry', 'Carpentry'),
        ('Electricity', 'Electricity'),
        ('Gardening', 'Gardening'),
        ('Home Machines', 'Home Machines'),
        ('House Keeping', 'House Keeping'),
        ('Interior Design', 'Interior Design'),
        ('Locks', 'Locks'),
        ('Painting', 'Painting'),
        ('Plumbing', 'Plumbing'),
        ('Water Heaters', 'Water Heaters'),
    )

class Service(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField()
    price_hour = models.DecimalField(decimal_places=2, max_digits=100)
    rating = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(5)], default=0)
    
    # creates a foreign key relation with users db using the username 
    # filed and applying a filter of a username not equal __ne to CUSTOMER
    username = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username', limit_choices_to={'role__ne':'CUSTOMER'})
    
    field = models.CharField(max_length=30, blank=False,null=False, choices=CHOICES)
    date = models.DateTimeField(auto_now=True, null=False)

    ## string identity of the class
    def __str__(self):
        return self.name
