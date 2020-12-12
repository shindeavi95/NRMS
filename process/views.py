from django.shortcuts import render
from process.forms import RegistrationForm
# Create your views here.

def showIndex(request):
    return render(request, 'process/main.html')


def Registration(request):
    rf = RegistrationForm(request.POST)
    if request.method == "POST":
        if rf.is_valid():
            rf.save()
        else:
            return render(request, "process/registration.html", {"form": rf})

    else:
      return render(request,"process/registration.html",{"form":rf})