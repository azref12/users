from django.urls import path, include
from . import views
from . views import *
from user import view_getuser
from rest_framework_simplejwt import views as jwt_views
from .customejwt import LogoutView, MyTokenObtainPairView
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path ('user/', views.User_list),
    path ('user/<int:pk>/', views.Users_details),
    path ('user/user_active/', views.Active_List),
    path ('user/getuser/', view_getuser.UserList.as_view(queryset=userdetail.objects.all(), 
                                                         serializer_class=UserSerializer), name='UserList'),
    path ('user/getuser/<int:pk>/', view_getuser.UserDetail.as_view(queryset=userdetail.objects.all(), 
                                                         serializer_class=UserSerializer), name='UserDetail')
]

urlpatterns += router.urls