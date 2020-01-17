from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('serve/', views.login_form, name="login_form")
]