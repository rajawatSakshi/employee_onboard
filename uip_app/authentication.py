# apps/management/authentication.py

from datetime import datetime, timedelta
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, ParseError

User = get_user_model()


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Extract the JWT from the Authorization header
        # import pdb;pdb.set_trace();
        jwt_token = request.META.get('HTTP_AUTHORIZATION')
        # import pdb; pdb.set_trace();
        if jwt_token is None:
            return None
        
        

        jwt_token = JWTAuthentication.get_the_token_from_header(jwt_token)  # clean the token

        # Decode the JWT and verify its signature
        try:
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed('Invalid signature')
        except:
            raise ParseError()

        # Get the user from the database
        emp_id = payload.get('emp_id')
        if emp_id is None:
            raise AuthenticationFailed('User identifier not found in JWT')
        
        user = User.objects.get(employee_id=emp_id)
        if user is None:
            raise AuthenticationFailed('User not found')

        # Return the user and token payload
        return user, payload

    def authenticate_header(self, request):
        return 'Bearer'

    @classmethod
    def create_jwt(cls, emp_id):
        current_time = datetime.utcnow()
        expiration_time = current_time + timedelta(hours=2)  # Extend token time by 2 hours
        payload = {
            'emp_id': emp_id,
            'exp': expiration_time,
            'iat': current_time,
        }

        # Encode the JWT with your secret key
        # print(payload)
        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return jwt_token

    @classmethod
    def get_the_token_from_header(cls, token):
        # print("hello")
        # import pdb; pdb.set_trace();
        token = token.replace('Bearer', '').replace(' ', '') if token is not None else None  # clean the token

        return token
