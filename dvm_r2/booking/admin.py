from django.contrib import admin
from .models import Passenger
from import_export.admin import ImportExportModelAdmin
from .resources import PassengerResource
# Register your models here.

@admin.register(Passenger)
class PassengerAdmin(ImportExportModelAdmin):
    resource_class = PassengerResource

    def save_model(self, request, obj, form, change):
        print("Save model method called")
        cancel_status = obj.cancel_status
        if cancel_status:
            obj.user.profile.wallet_balance += obj.fare
            obj.user.profile.save()
            print(f"Wallet balance updated: {obj.user.profile.wallet_balance}")


