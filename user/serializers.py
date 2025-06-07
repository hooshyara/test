from rest_framework import serializers
from .models import User

class UserSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'username', 'password', 'personal_code',
                   'fullName']

