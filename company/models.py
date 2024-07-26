from django.db import models
from user.models import User

# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to='image/')
    est_date = models.PositiveBigIntegerField( null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
