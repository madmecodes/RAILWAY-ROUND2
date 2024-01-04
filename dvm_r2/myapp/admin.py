from django import forms
from django.contrib import admin
from .models import Train

class TrainAdminForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = '__all__'
        widgets = {
            'runs_on': forms.CheckboxSelectMultiple,
        }

class TrainAdmin(admin.ModelAdmin):
    form = TrainAdminForm

admin.site.register(Train, TrainAdmin)
