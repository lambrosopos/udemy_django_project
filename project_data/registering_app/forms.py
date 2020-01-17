from django import forms
from registering_app.models import Members

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
    