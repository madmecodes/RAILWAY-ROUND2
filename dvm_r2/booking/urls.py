from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_form, name='booking_form'),
    path('submit/',views.booking_submit,name="booking_submit")
]
