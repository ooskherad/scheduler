from rest_framework.views import APIView
from rest_framework.response import Response

from permissions import IsOwnerOrReadOnly
from .models import User
from .serializers import UserSerializer
from rest_framework import status


class UserCreationView(APIView):
    def post(self, request, *args, **kwargs):
        data = UserSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    user = None

    def setup(self, request, *args, **kwargs):
        try:
            user_id = kwargs['id']
            self.user = User.objects.get(id=user_id)
        except Exception as error:
            self.errors = {'detail': error.args[0]}
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if not self.user:
            return Response(self.errors, status=status.HTTP_404_NOT_FOUND)
        data = UserSerializer(instance=self.user)
        return Response(data.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        if not self.user:
            return Response(self.errors, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, self.user)
        data = UserSerializer(instance=self.user, data=request.data, partial=True)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_200_OK)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
