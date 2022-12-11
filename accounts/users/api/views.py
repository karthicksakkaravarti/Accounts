from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer, SignupSerializer
import requests
User = get_user_model()

# Open API
class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            ser = SignupSerializer(data=request.data)
            if (ser.is_valid()):
                user_obj = ser.save()
                user_obj.set_password(request.data.get('password'))
                user_obj.save()
                return Response(ser.data)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(str(e))
            return Response({}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(RetrieveModelMixin,CreateModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False)
    def link_zwift(self, request):

        return Response(status=status.HTTP_200_OK, data=serializer.data)