from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserAPIList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        # user_id = self.request.data.get('user_id')
        # print(self.request.data)
        # print(self.kwargs)
        user_id = self.kwargs.get('user_id')
        return User.objects.filter(id=user_id)

    # def post(self, request):
    #     data = json.loads(request.body)
    #     print(data)
    #     serializer = UserSerializer(data=request.data, many=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'post': serializer.data})

# class UserAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
