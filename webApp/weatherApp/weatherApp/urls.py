
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Signup, name="signup"),
    path("login/", views.Login, name="login"),
    path("home/", views.Home, name="home"),
    path("logout/", views.Logout, name="logout"),
]
