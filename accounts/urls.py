from unicodedata import name
from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [
    path ('register/', views.registration_view),
]