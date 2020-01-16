from django import forms

class FormName(forms.Form):
    # objects = forms.ModelForm()
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)