from django import forms
from registering_app.models import Members

class NewMemberForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = "__all__"
    