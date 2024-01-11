from django.contrib import admin
from .models import Passenger
from import_export.admin import ImportExportModelAdmin
from .resources import PassengerResource
# Register your models here.

@admin.register(Passenger)
class PassengerAdmin(ImportExportModelAdmin):
    resource_class = PassengerResource
