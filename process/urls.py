from django.conf.urls.static import static
from django.urls import path

from RMS import settings
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
    path('logout/',views.logout, name= "logout"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('save_profile/', views.save_profile, name= "save_profile"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
