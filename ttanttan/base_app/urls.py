from django.urls import path, include
from base_app import views

app_name = 'base_app'

urlpatterns = [
    path('login/', views.user_login, name="user_login"),
]