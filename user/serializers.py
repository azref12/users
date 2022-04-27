from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import userdetail
         
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = userdetail
        fields = ['id_default','id','role','reward','point','coin','phone_number','created_at',
                  'app_id','code_status']

class RegistrationSerializer(serializers.ModelSerializer):
    id_users = UserSerializer (read_only=True, many=True)
    
    class Meta:
        model = User
        fields = ['id','id_users','password','last_login','is_superuser','username','first_name', 'last_name','email',
                  'is_staff','is_active','date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
        }