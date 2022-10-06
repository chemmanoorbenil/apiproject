from .models import *
from rest_framework import serializers





class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','id']




class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=Profile
        fields=['name','profile_img','about_me','cover_img']
