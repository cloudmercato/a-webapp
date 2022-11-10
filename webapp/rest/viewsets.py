from django.contrib.auth import models as auth_models
from rest_framework import viewsets
from rest import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = auth_models.User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = auth_models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
