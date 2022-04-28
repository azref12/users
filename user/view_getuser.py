from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import RegistrationSerializer, UserSerializer
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
# import datetime
from rest_framework import generics

if __name__ == "__main__": 
    print(userdetail.objects.all())

class UserList (generics.ListAPIView) :
        queryset = userdetail.objects.all()
        serializer_class = UserSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
        filterset_fields = ['id_default','id','code_status'] 
        ordering_fields = ['id_default','id','code_status']
        search_fields = ['id_default','id','code_status']

class UserDetail (generics.RetrieveUpdateDestroyAPIView) :
        queryset = userdetail.objects.all()
        serializer_class = UserSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
        filterset_fields = ['id_default','id','code_status'] 
        ordering_fields = ['id_default','id','code_status']
        search_fields = ['id_default','id','code_status']