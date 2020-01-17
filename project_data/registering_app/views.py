from django.shortcuts import render
from registering_app.forms import NewMemberForm

# Create your views here.
def index(request):
    return render(request, "registering_app/index.html")

def register(request):

    form = NewMemberForm()

    if request.method == "POST":
        form = NewMemberForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FROM INVALID FORM")

    return render(request, "registering_app/register.html", {"form":form})
