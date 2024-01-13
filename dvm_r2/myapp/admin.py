# admins.py
from django import forms
from django.contrib import admin
from .models import Train,Station

class TrainAndStationAdminArea(admin.AdminSite):
    site_header = 'TranStationAdminArea'

TrainAndStationAdminArea_site = TrainAndStationAdminArea(name="trainAndStation")

admin.site.register(Train)
admin.site.register(Station)
TrainAndStationAdminArea_site.register(Train)
TrainAndStationAdminArea_site.register(Station)