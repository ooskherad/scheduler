from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.serializers import UserSerializer
from .serializers import SchedulerSerializer
from .models import Scheduler


class SchedulerRegistration(LoginRequiredMixin, APIView):
    def post(self, request):
        scheduler = Scheduler.objects.filter(user=request.user)
        if scheduler:
            return Response(data={'detail': 'you are scheduler before!!'}, status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        user = UserSerializer(instance=request.user, data={'email': data.get('email')}, partial=True)
        if user.is_valid():
            user.save()
            data.update(user_id=user.instance.id)
            scheduler = SchedulerSerializer(data=data)
            if scheduler.is_valid():
                scheduler.save()
        return Response(status=status.HTTP_201_CREATED)
