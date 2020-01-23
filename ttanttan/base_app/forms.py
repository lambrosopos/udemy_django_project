from django import forms
from django.contrib.auth.models import User
from base_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
    
class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolioSite', 'profilePic')

        widgets = {
            'portfolioSite':forms.URLInput(attrs={'class':'form-control'}),
            'profilePic':forms.FileInput(attrs={'class':'custom-file-input'}),
        }