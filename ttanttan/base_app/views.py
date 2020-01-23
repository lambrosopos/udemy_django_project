from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView
from base_app.forms import UserForm, UserProfileInfoForm

# Create your views here.
class IndexView(View):
    
    def get(self, request):
        return render(request, "base_app/index.html")


class LoginView(View):

    def get(self, request):
        return render(request, "base_app/login.html")


class RegisterView(View):

    def get(self, request):
        registered = False

        user_form = UserForm()
        profile_form = UserProfileInfoForm()

        context_dict = {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered' : registered,
        }

        return render(request, "base_app/registration.html", context=context_dict)