from .models import *
from rest_framework import serializers





class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='_all_'




class ProfileSerializer(serializers.ModelSerializer):
    category=UserSerializers()
    class Meta:
        model=Profile
        fields='_all_'

