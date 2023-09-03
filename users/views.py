from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from users.models import user
from users.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = user.objects.check()
    serializer_class = UserSerializer


