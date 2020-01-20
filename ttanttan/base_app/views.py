from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "base_app/index.html")


def user_login(request):
    return render(request, "base_app/login.html")