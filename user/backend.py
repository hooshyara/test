from django.contrib.auth.backends import ModelBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User

class PhoneBackend(ModelBackend):
    def authenticate(self, request, username, password= None, **kwargs):
        try:
            user = User.objects.get(username= username)
        except User.DoesNotExist:
            pass