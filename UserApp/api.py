from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import permission_classes


# This file contains API views for user authentication, including user creation,
# login, and a protected view that requires authentication.

@api_view(['POST'])
def UserCreateApi(request):
    username = request.data['username']
    password = request.data['password']

    User.objects.create_user(username = username, password = password)
    return Response ({
        'message': 'User created'
    })

# @api_view(['POST'])
# def UserLoginApi(request):
#     username = request.data['username']
#     password = request.data['password']

#     user = authenticate(username = username, password = password)
#     if user is not None:
#         # login(request, user)

#         token,created = Token.objects.get_or_create(user = user)
#         return Response({
#             'message': 'user logged in',
#             'token': token.key
#         })
#     else:
#         return Response({
#             'message': 'Invalid credentials'
#         })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protectedView(request):
        return Response({ 
            'message': 'I am already authenticated',
            'username': request.user.username
        })