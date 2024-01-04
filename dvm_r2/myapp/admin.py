# admins.py
from django import forms
from django.contrib import admin
from .models import Train


admin.site.register(Train)
