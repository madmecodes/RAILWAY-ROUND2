from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="myapp-home"),
    path('train/<str:train_number>/',views.train_details,name="train_details")
]