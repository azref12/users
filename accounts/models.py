from django.db import models
from django.contrib.auth.models import User

class userdetail (models.Model):
    id_default = models.AutoField(primary_key=True)
    id = models.ForeignKey(User, related_name='id_users', on_delete=models.CASCADE)
    role = models.IntegerField(blank=False, null=True, default=4)
    reward = models.IntegerField(blank=False,default=0)
    point = models.IntegerField(blank=False,default=0)
    coin = models.IntegerField(blank=False,default=0)
    phone_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    app_id = models.IntegerField(blank=False,default=0)
    code_status = models.IntegerField(blank=False, null=True, default=0) 
