from django.shortcuts import render
from registering_app.forms import NewMemberForm
from django import forms

# Create your views here.
def index(request):
    return render(request, "registering_app/index.html")

def register(request):

    form = NewMemberForm()

    if request.method == "POST":
        form = NewMemberForm(request.POST)

        if form.is_valid():
            print("Form========================================", form)
            form.save(commit=True)
            return index(request)
        else:
            return render(request, "registering_app/register.html", {"message": "Passwords don't match!"})

    return render(request, "registering_app/register.html", {"form":form})
