from django import forms
from process.models import *
import random
from process.utils import sendTextMessage


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_otp(self):
        cno = self.cleaned_data['contact']
        # otp = self.cleaned_data['otp']
        random_number = random.randint(100000, 999999)
        message = 'This is Avinash and this message is for only test and your OTP is' + str(random_number)
        sendTextMessage(message, cno)
        print(random_number)
        # print(cno)
        return random_number

    class Meta:
        model = RegistrationModel
        exclude = ('status',)
