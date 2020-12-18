from django.shortcuts import render, redirect
from process.forms import RegistrationForm
from process.models import RegistrationModel,ProfileModel,IndustriesModel
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
        if result.status == "pending":
            return render(request, "process/login.html", {"error": "Sorry Your Account is not Approved yet"})
        elif result.status == "closed":
            return render(request, "process/login.html", {"error": "Sorry Your Account is Closed"})
        else:
            request.session["contact"] = result.contact
            request.session["name"] = result.name
            request.session["rno"] = result.rno
            return redirect('view_profile')

    except RegistrationModel.DoesNotExist:
        return render(request, 'process/login.html', {"error":"Invalid Username Or Password"})


def view_profile(request):
    rno = request.session["rno"]
    try:
        r_no = ProfileModel.objects.get(person__rno=rno)
        status = True
    except ProfileModel.DoesNotExist:
        status = False
    return render(request, "process/view_profile.html",{"status":status, 'r_no': r_no})
    

def logout(request):
    try:
        del request.session["contact"]
        del request.session["name"]
        del request.session["rno"]
        return redirect("main_page")
    except KeyError:
        return render(request, "process/login.html",{"error":"Please Do Login First"})


def update_profile(request):
    # try:
    #     result = IndustriesModel.objects.getList("ino")
    #     status = True
    # except IndustriesModel.DoesNotExist:
    #     status = False
    # return render(request, "process/update_profile.html",{"status":status})
    # result = ProfileModel.objects.get(itype__ino=ino)

    # result = IndustriesModel.objects.all(ino=no)
    result = IndustriesModel.objects.all().order_by('-ino')[:50]
    return render(request, "process/update_profile.html", {"data":result})


def save_profile(request):
    # idata = IndustriesModel.objects.all().order_by('-ino')[:50]
    rno = request.POST.get("t1")
    education = request.POST.get("t2")
    photo = request.FILES.get("t3")
    resume = request.FILES.get("t4")
    # email = request.POST.get("t5")
    # contact = request.POST.get("t6")
    industry_id = request.POST.get("t5")   # we are getting here , Aggri
    # industry = IndustriesModel.objects.get(ino=industry_id)
    print(industry_id)
    result = ProfileModel(person_id=rno, education=education, photo=photo, resume=resume, itype_id=industry_id)
    result.save()
    # obj = IndustriesModel.objects.create(itype=type)
    # obj.save()
    # iresult = IndustriesModel(itype=itype)
    # iresult.save()
    return redirect("view_profile")


