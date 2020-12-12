
from django.urls import path

from process import views

urlpatterns = [
    path('',views.showIndex, name= "main_page"),
    path('registration/',views.Registration,name="registration"),
    path('user_registration',views.Registration,name="user_registration"),
    path('user_otp/', views.user_OTP, name= "user_otp"),
]
