from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts import views

# Create your views here.

class signUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')

    template_name = 'accounts/signup.html'

    
