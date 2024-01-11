from import_export import resources
from .models import Passenger

class PassengerResource(resources.ModelResource):
    class Meta:
        model = Passenger
        fields = ('id', 'user', 'train_number', 'ticket_type', 'fare', 'cancel_status', 'passenger_first_name', 'passenger_age', 'travel_date', 'booking_date')
