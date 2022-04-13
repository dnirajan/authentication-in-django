from django.contrib import admin
from .models import CreateUser


# Register your models here.
@admin.register(CreateUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'dob', 'gender', 'mobile', 'email']
