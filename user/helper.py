from .models import User
from random import randint
import datetime
import jwt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken


def get_user(token):
    try:
        payload = jwt.decode(str(token), options={"verify_signature": False})
        # print(f'user token: {token}')
        print(payload['user_id'],'\t-\t', payload)
        if payload['exp'] >= int(datetime.datetime.now().timestamp()) and  OutstandingToken.objects.get(token=token).DoesNotExist:
            user = User.objects.get(id=payload['user_id'])
            return user
        else:
            print('token expired')
            out_token = OutstandingToken.objects.get(token=token)
            out_token.delete()
            return None
    except Exception as e:
        print(f'error: {e}')
        return None
