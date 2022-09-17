from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.contrib.auth import logout

from account.serializers import UserSerializer
from account.models import User


@api_view(['POST'])
def register_user(request, format=None):
    try:
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()
            account.is_active = True
            account.save()

            token, _ = Token.objects.get_or_create(user=account)

            response = {
                'message': 'User registered successfully',
                'username': account.username,
                'email': account.email,
                'token': token.key,
            }

            return Response(response, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except IntegrityError as err:
        return Response(err.__str__(), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def logout_user(request):
    request.user.auth_token.delete()
    logout(request)

    return Response('User logged out successfully')


@api_view(['GET'])
def user_list(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
