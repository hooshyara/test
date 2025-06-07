from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
import datetime

class CustomAuth(JWTAuthentication):
    def authenticate(self, request):
        token = self.get_token_from_request(request)

        if token is None:
            return None

        print(token, 'this is the authenitcation file')
        
        if token.payload['exp'] < int(datetime.now().timestamp()):
            RefreshToken(token).blacklist()

            return None

        return self.get_user(token), token

        