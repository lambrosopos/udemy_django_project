from django import forms
from django.contrib.auth.models import User
from registering_app.models import Members, UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ("portfolio_site", "profile_pic")

class NewMemberForm(forms.ModelForm):
    verifyPassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Members
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data["password"]
        vPassword = cleaned_data["verifyPassword"]

        if password and vPassword:
            if password != vPassword:
                raise forms.ValidationError("Passwords don't match")
    