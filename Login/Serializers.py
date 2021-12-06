from django.contrib.auth.models import User
from drf_queryfields import QueryFieldsMixin
from rest_framework import serializers


class UserSerializers(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

