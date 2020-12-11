from django import forms
from process.models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationModel
        exclude = ('otp',)

