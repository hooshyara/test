from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


def generate_jwt_token(user):
    print(user)

    refresh = RefreshToken.for_user(user)
    refresh_tocken = str(refresh.access_token)
    access_token = str(refresh)
    return refresh_tocken, access_token

    