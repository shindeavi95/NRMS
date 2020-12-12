from django.shortcuts import render, redirect
from process.forms import RegistrationForm


# Create your views here.

def showIndex(request):
    return render(request, 'process/main.html')


def Registration(request):
    print("=============1=============")
    rf = RegistrationForm(request.POST)
    if request.method == "POST":
        print("=============3=============")
        if rf.is_valid():
            print("===========4===============")
            rf.save()
            print("=============5=============")
            return redirect('user_otp')
        else:
            print("=============6=============")
            return render(request, "process/registration.html", {"form": rf})

    else:
        print("=============2=============")
        return render(request, "process/registration.html", {"form": rf})


def user_OTP(request):
    return render(request, "process/otp.html")
