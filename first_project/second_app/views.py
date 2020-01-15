from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    
    return HttpResponse("<em>Hello World Emphasis</em>")


def help(request):
  help_dictionary = {
    'insert_help' : "What would  you like help with?"
  }
  return render(request, 'second_app/help.html', context=help_dictionary)
