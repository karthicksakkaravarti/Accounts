from . import (Serializers)
from django.contrib.auth.models import User
from rest_framework import viewsets


class UserAPI(viewsets.ModelViewSet):
    serializer_class = Serializers.UserSerializers
    queryset = User.objects.all()
