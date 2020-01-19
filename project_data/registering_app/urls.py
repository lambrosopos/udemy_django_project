from django.urls import path
from registering_app import views

app_name = 'registering_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
]