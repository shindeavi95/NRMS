from django.shortcuts import render

# Create your views here.

def showIndex(request):
    return render(request,'process/index.html')
