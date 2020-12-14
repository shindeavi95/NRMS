from django.urls import path

from process import views

urlpatterns = [
    path('', views.showIndex, name="main_page"),
    path('registration/', views.Registration, name="registration"),
    path('user_registration/', views.Registration, name="user_registration"),
    path('user_otp/', views.user_OTP, name="user_otp"),
    path('validate_otp/', views.validate_otp, name="validate_otp"),
    path('conformation/', views.conformation, name="conformation"),
    path('login/', views.login, name="login"),
    path('login_check/', views.login_check, name="login_check"),
    path('view_profile/', views.view_profile, name="view_profile"),
    path('logout/',views.logout, name= "logout")
]
