from django.db import models

# Create your models here.

DAYS_OF_WEEK_CHOICES = [
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('Th', 'Thursday'),
        ('F', 'Friday'),
        ('Sa', 'Saturday'),
        ('Su', 'Sunday'),
]
class Train(models.Model):
    train_number= models.CharField(max_length=10,unique=True)
    train_name = models.CharField(max_length=100,unique=True)
    from_station_code= models.CharField(max_length=50)
    to_station_code = models.CharField(max_length=50)
    total_seats_1ac = models.IntegerField(default=30)
    total_seats_2ac = models.IntegerField(default=30)
    total_seats_3ac = models.IntegerField(default=30)
    fare_1ac = models.IntegerField(default=50)
    fare_2ac = models.IntegerField(default=100)
    fare_3ac = models.IntegerField(default=200)
    train_available = models.BooleanField(default=True)
    runs_on = models.CharField(max_length=14, choices=DAYS_OF_WEEK_CHOICES)
    def __str__(self):
        return f"{self.train_number} - {self.train_name}"


