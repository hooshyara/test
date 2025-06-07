from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    fields  = ['phone', 'username', 'password', 'personal_code', 'fullName', 'company']
    list_display = ['id', 'fullName']
    