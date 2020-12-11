from django.shortcuts import render
from process.forms import RegistrationForm
# Create your views here.

def showIndex(request):
    return render(request, 'process/main.html')


def Registration(request):
    rf = RegistrationForm()
    if request.method == "POST":
        pass
    else:
      return render(request,"process/registration.html",{"form":rf})