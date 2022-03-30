import random

from rest_framework.views import APIView
from rest_framework.response import Response

from permissions import IsOwnerOrReadOnly
import utils
from .models import User, OtpCode
from .serializers import UserSerializer
from rest_framework import status


class UserRegistrationVerifyOtpView(APIView):
    def post(self, request, *args, **kwargs):
        user_session = request.session['user_registration_info']
        otp_code = OtpCode.objects.get(mobile=user_session['mobile'])
        user_otp_code = request.data['code']
        if str(otp_code.code) == user_otp_code:
            User.objects.create_user(mobile=user_session['mobile'], password=user_session['password'])
            OtpCode.objects.filter(mobile=user_session['mobile']).delete()
            return Response(status=status.HTTP_201_CREATED)
        return Response(data={'details': 'Wrong Code'}, status=status.HTTP_400_BAD_REQUEST)


class UserCreationView(APIView):
    def post(self, request, *args, **kwargs):
        data = UserSerializer(data=request.data)
        if data.is_valid():
            random_code = random.randint(1000, 9999)
            utils.send_otp_code()
            OtpCode.objects.create(mobile=request.data['mobile'], code=random_code)
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
        data = UserSerializer(instance=self.user, data=request.data, partial=True)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_200_OK)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
