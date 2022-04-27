from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from datetime import timedelta

from accounts.serializers import *
from accounts.models import userdetail
from django.contrib.auth.models import User
from django.conf import settings


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        print('ini self:')
        print(self)
        print('ini attrs:')
        print(attrs)

        data = super().validate(attrs)

        refresh = RefreshToken.for_user(self.user)
        access_token = refresh.access_token
        access_token.set_exp(lifetime=timedelta(days=10))
        data['token'] = str(access_token)
        data['username'] = self.user.username
        data['is_superuser'] = self.user.is_superuser
        data['is_staff'] = self.user.is_staff
        data['id'] = self.user.id
        data['firstName'] = self.user.first_name
        data['lastName'] = self.user.last_name
        data['password'] = self.user.password

        if self.user.is_staff == False:
            id_user = userdetail.objects.get(id_users_id=self.user.id).role
            data['role'] = id_user
        else:
            data['role'] = 1
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
