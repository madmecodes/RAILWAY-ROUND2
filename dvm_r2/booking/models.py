from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Passenger(models.Model):
    user= models.ForeignKey(User,on_delete =models.CASCADE)
    train_number = models.CharField(max_length=100)
    ticket_type = models.CharField(max_length=100)
    fare = models.IntegerField()
    cancel_status = models.BooleanField(default=False)
    passenger_first_name = models.CharField(max_length=255)
    passenger_age = models.CharField(max_length=20)
    travel_date = models.DateField(default=timezone.now)
    booking_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"passenger- {self.passenger_first_name}-by-{self.user}"