from django.contrib.auth.models import User
from rest_framework import Response

def UserCreateApi(request):
    Username = request.data['username']
    password = request.data['password']

    User.objects.create_user(username = username, password = password)
    return Response ({
        'message': 'User created'
    })
