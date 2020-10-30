from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model=CustomUser
    list_display=["username","email","is_staff"]

admin.site.register(CustomUser,CustomUserAdmin)

