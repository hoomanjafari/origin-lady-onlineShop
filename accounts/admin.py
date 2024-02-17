from django.contrib import admin
from .models import MyUser, UserAddress


admin.site.register(MyUser)
admin.site.register(UserAddress)
