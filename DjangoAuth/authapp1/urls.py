from django.urls import path
from . import views
from django.contrib.auth import views as authentication_view

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', authentication_view.LoginView.as_view(template_name="authapp1/login.html"), name="login"),
    path('logout/', authentication_view.LogoutView.as_view(template_name="authapp1/logout.html"), name="logout"),
    path('detail/<str:slug>', views.detail, name="detail"),
]