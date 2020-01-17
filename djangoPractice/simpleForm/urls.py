from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_form, name="login_form")
]