from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="myapp-home"),
    path('train/',views.train_details,name="train_details")
]