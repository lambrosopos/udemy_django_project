from django.urls import path
from registering_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
]