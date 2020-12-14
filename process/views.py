from django.shortcuts import render, redirect
from process.forms import RegistrationForm
from process.models import RegistrationModel
from django.contrib.messages import success


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


def validate_otp(request):
    try:
        result = RegistrationModel.objects.get(contact=request.POST.get("t1"), otp=request.POST.get("t2"))
        if result.status == "pending":
            result.status = "Approved"
            result.save()
            success(request, "Thanks For Your Registration")
            return redirect("conformation")

        elif result.status == "Approved":
            success(request, "Your Registration Is Already Approved, Please Do Login")
            return redirect("conformation")

    except RegistrationModel.DoesNotExist:
        message = "Sorry Invalid OTP Please try Again"
        return render(request, "process/otp.html", {"message": message})


def conformation(request):
    return render(request, "process/conformation.html")


def login(request):
    return render(request, "process/login.html")


def login_check(request):
    try:
        result = RegistrationModel.objects.get(email=request.POST.get("u1"), password=request.POST.get("u2"))
        request.session["contact"] = result.contact
        request.session["name"] = result.name

    except RegistrationModel.DoesNotExist:
        return None


def view_profile(request):
    return render(request, "process/view_profile.html")