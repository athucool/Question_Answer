from .serializers import CustomUserSerializerz
from rest_framework.views import APIView
from rest_framework.response import Response


class CustomeUserApiView(APIView):
    def get(self,request):
        serializer =CustomUserSerializerz(request.user)
        return Response(serializer.data)
        

