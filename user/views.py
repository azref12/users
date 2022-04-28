from threading import local
from rest_framework.permissions import AllowAny, IsAuthenticated
from inspect import isfunction
from msilib.schema import AppId
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import RegistrationSerializer, UserSerializer
from django.contrib.auth.models import User
from accounts.models import userdetail
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
import datetime
from pathlib import Path
from decouple import Config ,RepositoryEnv, Csv
import os
from re import X
from django.db import DatabaseError, transaction
from django.db.utils import IntegrityError

t = datetime.datetime.now()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_FILE = './config/.env'
getenv = Config(RepositoryEnv(DOTENV_FILE))
APP_ID=getenv('APP_ID')

if __name__ == "__main__":
    print(userdetail.objects.all())

mastermodel = isfunction
masterserialzer = isfunction

@csrf_exempt
@api_view(["GET","POST"])
@permission_classes([AllowAny])

def User_list (request):    
        
        mastermodel = User
        masterserialzer = RegistrationSerializer
                        
        mymodels = userdetail
        serializerss = UserSerializer

        if request.method == 'GET':
                localmodel = mastermodel.objects.all()
                localserializer = masterserialzer(localmodel, many=True)
                
                localmodels = mymodels.objects.all()
                localserializers = serializerss (localmodels, many=True)
                
                formater = {
                        "master" : localserializer.data
                }
                return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : formater},
                                status=201)
                
        if request.method == 'POST':
                localrequest = JSONParser().parse(request)
                localserializer = masterserialzer (data=localrequest)        
                with transaction.atomic():
                        sid = transaction.savepoint()
                        try:
                                if localserializer.is_valid():
                                                
                                        id_users = userdetail.objects.filter(id = localrequest['id']).first()
                                        details = userdetail (
                                                id = id_users,
                                                id_default = localrequest.data.get['id_role'],
                                                role = localrequest.data.get['role'],
                                                reward = localrequest.data.get['reward'],
                                                point = localrequest.data.get['point'],
                                                coin = localrequest.data.get['coin'],
                                                phone_number = localrequest.data.get['phone_number'],
                                                app_id = APP_ID,
                                                code_status = localrequest.get['code_status']
                                        )
                                        details.save()
                                transaction.savepoint_commit(sid)
                        except IntegrityError:
                                transaction.savepoint_rollback(sid)
                                        
                        mymodels = userdetail.objects.all() 
                        serializerss = UserSerializer (mymodels, many=True)
                                        
                        formater = {
                                "detail" : serializerss.data
                        }
                                
                        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : formater},
                                        status=201) 
        return JsonResponse(localserializer.errors, status=400)

@csrf_exempt
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([AllowAny])  
def Users_details (request, pk):
        
        mastermodel = User
        masterserialzer = RegistrationSerializer
        
        mymodels = userdetail
        serializerss = UserSerializer

        if request.method == 'GET':
        
                localmodel = mastermodel.objects.filter(id=pk)
                localserializers = masterserialzer (localmodel, many=True)
                
                formater = {
                        "master": localserializers.data
                }
                return JsonResponse({'message': 'successfully', 'status': True, 'count': 1, 
                                     'results': formater})
        
        elif request.method == 'PUT': 
                localrequest = JSONParser().parse(request)
                localserializer = masterserialzer(data=localrequest) 

                if localserializer.is_valid(): 
                
                        localserializer.save()  
                
                        localmodel = mastermodel.objects.all()
                        localserializer = masterserialzer(localmodel, many=True)

                        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 
                                             'results' : localserializer.data}, status=201)
                return JsonResponse(localserializer.errors, status=400)
        
@csrf_exempt
@api_view(["GET"])
@permission_classes([AllowAny])
def Active_List (request):

        if request.method == 'GET':
                with transaction.atomic():
                        sid = transaction.savepoint()
                        try:
                                cek = request.GET['status']
                                if cek == '/is_nonactive':
                                        localmodeldetail = userdetail.objects.filter (code_status=0)
                                        localserializersdetail = UserSerializer (localmodeldetail, many=True)

                                        return JsonResponse({'results': localserializersdetail.data}) 
                                
                                if cek == '/is_active':
                                        localmodeldetail = userdetail.objects.filter (code_status=1)
                                        localserializersdetail = UserSerializer (localmodeldetail, many=True)

                                        return JsonResponse({'results': localserializersdetail.data})
                                
                                if cek == '/is_verify':
                                        localmodeldetail = userdetail.objects.filter (code_status=2)
                                        localserializersdetail = UserSerializer (localmodeldetail, many=True)

                                        return JsonResponse({'results': localserializersdetail.data})
                                
                                if cek == '/is_banned':
                                        localmodeldetail = userdetail.objects.filter (code_status=3)
                                        localserializersdetail = UserSerializer (localmodeldetail, many=True)

                                        return JsonResponse({'results': localserializersdetail.data})
                                
                                if cek == '/is_delete':
                                        localmodeldetail = userdetail.objects.filter (code_status=4)
                                        localserializersdetail = UserSerializer (localmodeldetail, many=True)

                                        return JsonResponse({'results': localserializersdetail.data})  
                                         
                                transaction.savepoint_commit(sid)
                        except IntegrityError:
                                transaction.savepoint_rollback(sid)