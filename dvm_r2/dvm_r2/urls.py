from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from users.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path("register/", user_views.register, name="register"),
    path("login/",auth_views.LoginView.as_view(template_name="users/login.html", authentication_form=LoginForm),name="login"),
    path("logout/",user_views.logout,name="logout")

]
