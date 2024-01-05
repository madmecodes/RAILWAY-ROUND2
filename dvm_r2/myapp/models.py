from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

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
    runs_on = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.train_number} - {self.train_name}"

class Station(models.Model):
    train = models.ForeignKey(Train,on_delete=models.CASCADE)
    train_number = models.CharField(max_length=10,default='')  
    station_code = models.CharField(max_length=100)
    station_name= models.CharField(max_length=100)
    distance = models.IntegerField()
    arrival_time = models.TimeField()
    halt_time = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.train.train_number} - {self.station_code} - {self.station_name}"
