from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success")
            print(f"Name : {form.cleaned_data['name']}")
            print(f"Email : {form.cleaned_data['email']}")
            print(f"Text : {form.cleaned_data['text']}")
            

    return render(request, 'basicapp/form_page.html', context={'form':form})

