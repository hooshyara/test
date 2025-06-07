from django.urls import path
from .views import *

app_name = 'company'

urlpatterns = [
    path('', CompanyView.as_view(), name='company'),
    path('ed/<int:id>/', CompanyView.as_view(), name='company-edit'),
    
]