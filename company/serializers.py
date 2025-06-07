from rest_framework import serializers
from .models import Company

class CompanySeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'commission', 'commission_intermediary', 
                  'bill_insurance']

