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
        return render(request, "base_app/registration/login.html")


def registerView(request):
    
        registered = False

        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileInfoForm(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                
                if 'profilePic' in request.FILES:
                    profile.profilePic = request.FILES['profilePic']
                
                profile.save()

                registered = True
            
            else:
                print('Invalid User Approach')
        
        else:
            user_form = UserForm()
            profile_form = UserProfileInfoForm()

        context_dict = {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered' : registered,
        }

        return render(request, "base_app/registration/registration.html", context=context_dict)