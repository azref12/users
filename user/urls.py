from django.urls import path, include
from . import views
from . views import *
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
]

urlpatterns += router.urls