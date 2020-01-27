from django.urls import path, include
from base_app import views

app_name = 'base_app'

urlpatterns = [
    path('register/', views.registerView, name="register"),
]