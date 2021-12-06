from rest_framework.response import Response

from . import (Serializers)
from django.contrib.auth.models import User
from rest_framework import viewsets


class UserAPI(viewsets.ReadOnlyModelViewSet):
    serializer_class = Serializers.UserSerializers
    queryset = User.objects.all()
    pagination_class = None

    def get_queryset(self):
        return [self.request.user]

    def list(self, request, *args, **kwargs):
        return Response(super().list(request, *args, **kwargs).data[0]) if len(super().list(request, *args, **kwargs).data) == 1 else super().list(request, *args, **kwargs)







