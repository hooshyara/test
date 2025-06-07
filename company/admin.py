from django.contrib import admin
from .models import Company, MainCompany

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    model = Company
    
    list_display = ['id', 'name']

@admin.register(MainCompany)
class MainCompanyAdmin(admin.ModelAdmin):
    model = MainCompany
    
    list_display = ['id']


