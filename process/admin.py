from django.contrib import admin
from process.models import IndustriesModel
from django.contrib.auth.models import Group,User
from .models import ProfileModel

admin.site.register(IndustriesModel)

admin.site.unregister(Group)
admin.site.unregister(User)
