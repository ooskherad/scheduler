import random

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from permissions import IsOwnerOrReadOnly
from .models import User, OtpCode
from .serializers import UserSerializer
from rest_framework import status
from services.otp_service import OtpService


class UserLogin(APIView):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('accounts:profile')

    def post(self, request):
        data = request.data
        try:
            user = authenticate(username=data['mobile'], password=data['password'])
            if user is not None:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(data={'detail': 'Wrong UserName or password'}, status=status.HTTP_401_UNAUTHORIZED)
        except KeyError as exception:
            return Response(data={'error': f'{exception.args[0]} required'}, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationVerifyOtpView(APIView):

    def post(self, request, *args, **kwargs):
        user_session = request.session['user_registration_info']
        if OtpService.check_code(user_session['mobile'], int(request.data['code'])):
            User.objects.create_user(mobile=user_session['mobile'], password=user_session['password'])
            OtpCode.objects.filter(mobile=user_session['mobile']).delete()
            return Response(status=status.HTTP_201_CREATED)
        return Response(data={'details': 'Wrong Code'}, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView(APIView):

    def post(self, request, *args, **kwargs):
        data = UserSerializer(data=request.data)
        if data.is_valid():
            OtpService.check(request.data['mobile'])
            request.session['user_registration_info'] = {
                'mobile': request.data['mobile'],
                'password': request.data['password']
            }
            return Response(status=status.HTTP_200_OK)
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
        user = UserSerializer(instance=self.user, data=request.data, partial=True)
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_200_OK)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfile(APIView):
    def get(self, request):
        return Response(data={'detail': "profile"})
