from django.contrib import admin
from .models import Passenger
from import_export.admin import ImportExportModelAdmin
from .resources import PassengerResource
from myapp.models import Train
# Register your models here.

@admin.register(Passenger)
class PassengerAdmin(ImportExportModelAdmin):
    resource_class = PassengerResource

    def save_model(self, request, obj, form, change):
        cancel_status = obj.cancel_status
        super().save_model(request, obj, form, change)
        if cancel_status:
            obj.user.profile.wallet_balance += obj.fare
            obj.user.profile.save()
            try:
                train = Train.objects.get(train_number=obj.train_number)
            except Train.DoesNotExist:
                train = None
            if train:
                if obj.ticket_type == '1AC':
                    train.total_seats_1ac += 1
                elif obj.ticket_type == '2AC':
                    train.total_seats_2ac += 1
                elif obj.ticket_type == '3AC':
                    train.total_seats_3ac += 1
                train.save()
        if cancel_status==False:
            obj.user.profile.wallet_balance -= obj.fare
            obj.user.profile.save()
            print(f"Wallet balance updated: {obj.user.profile.wallet_balance}")
            try:
                train = Train.objects.get(train_number=obj.train_number)
            except Train.DoesNotExist:
                train = None
            if train:
                if obj.ticket_type == '1AC':
                    train.total_seats_1ac -= 1
                elif obj.ticket_type == '2AC':
                    train.total_seats_2ac -= 1
                elif obj.ticket_type == '3AC':
                    train.total_seats_3ac -= 1
                train.save()


