from rest_framework import serializers
from videoapp.models import *
from django.contrib.auth.models import User

class VideoSerializer(serializers.ModelSerializer):
    #publisher = serializers.CharField(source="User.username",read_only=True)
    class Meta:
        model = Video
        fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
    #publisher = serializers.CharField(source="User.username",read_only=True)
    class Meta:
        model = User
        fields ='__all__'

