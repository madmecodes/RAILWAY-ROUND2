from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="myapp-home"),
    path('train/',views.train_details,name="train_details"),
    path('choose_train/',views.choose_train,name="choose_train"),
    path('choose_train_list',views.choose_train_list,name="choose_train_list")
]