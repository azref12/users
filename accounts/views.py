from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .serializers import *
from .models import *
from django.contrib.auth.hashers import make_password
# from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
def registration_view (request):

    if request.method == 'GET':
        localmodel = userdetail.objects.all()
        localserializer = RegistrationSerializer(localmodel, many=True)
        # print(localserializer)
        return JsonResponse({'message': 'successfully', 'status': True, 'count': 1, 'results': localserializer.data})

    if request.method == 'POST':
        localrequest = JSONParser().parse(request)
        localserializer = RegistrationSerializer(data=localrequest)
        print(localrequest)
        print(localserializer)
        if localserializer.is_valid():
            emaildata = localserializer.data['email']
            localmodels = userdetail.objects.filter(email=emaildata)

            usernamedata = localserializer.data['username']
            localmodelsuser = userdetail.objects.filter(username=usernamedata)

            if len(localmodels) == 0:

                if len(localmodelsuser) == 1:
                    return JsonResponse({'success': False, "isRegistered": True,
                                         "message": "Username  Anda Telah Terdaftar", })

                else:

                    account = userdetail(
                        email=localserializer.data.get('email'),
                        username=localserializer.data.get('username'),
                        firstname=localserializer.data.get('firstname'),
                        lastname=localserializer.data.get('lastname'),
                        password=make_password(
                            localserializer.data.get('password')),
                    )
                    account.save()
                    return JsonResponse({'success': True, "isRegistered": False,
                                        "message": "Email verifikasi berhasil terkirim", })

            else:
                return JsonResponse({'success': False, "isRegistered": True,
                                    "message": " Email Anda Telah Terdaftar", })

        else:
            localserializer.errors
            return JsonResponse({'success': False, "isRegistered": False,
                                "message": "Email verifikasi gagal terkirim", })

