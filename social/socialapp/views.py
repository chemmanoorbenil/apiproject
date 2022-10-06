from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.


class Register_user(APIView):
    def get(self, request):
        student_obj = Profile.objects.all()
        serializer = ProfileSerializer(student_obj, many=True)
        return Response({'status': 200, 'payload': serializer.data})
