# admins.py
from django import forms
from django.contrib import admin
from .models import Train,Station


admin.site.register(Train)
admin.site.register(Station)
