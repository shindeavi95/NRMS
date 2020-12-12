from django import forms
from process.models import *
import random

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_otp(self):
        otp = self.cleaned_data['otp']
        random_number = random.randint(100000,999999)
        return random_number
    class Meta:
        model = RegistrationModel
        exclude = ('status',)

