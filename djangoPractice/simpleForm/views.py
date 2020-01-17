from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "simpleForm/index.html")


def login_form(request):
    pass
