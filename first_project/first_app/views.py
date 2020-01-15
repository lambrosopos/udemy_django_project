from django.shortcuts import render

# Create your views here.

from  django.http import HttpResponse

def index(request):
    my_dictionary = {'insert_me': "Hello, this is views.py"}
    return render(request, 'first_app/index.html', context=my_dictionary)