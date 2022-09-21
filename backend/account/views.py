from rest_framework.decorators import api_view
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404

from account.serializers import UserSerializer
from account.models import User
from helpers.pagination import get_paginted_result


class LoginUser(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'id': user.pk,
            'email': user.email,
            'username': user.username,
        })


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
                'id': account.id,
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
        PAGE_SIZE = 10

        return get_paginted_result(queryset=users, request=request,
                                   page_size=PAGE_SIZE, serializer=UserSerializer)


@api_view(['GET'])
def who_am_i(request, format=None):
    if request.method == 'GET':
        user = get_object_or_404(User, email=request.user)
        serilizer = UserSerializer(user)

        return Response(serilizer.data, status=status.HTTP_200_OK)
