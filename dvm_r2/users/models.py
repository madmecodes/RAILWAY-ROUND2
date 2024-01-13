from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet_balance= models.DecimalField(max_digits=10,decimal_places=0,default=50,validators=[MinValueValidator(0)])
    
    def __str__(self):
        return f'{self.user.username} Profile' 
    

