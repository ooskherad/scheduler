from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.serializers import UserSerializer
from .serializers import SchedulerSerializer, ServiceSerializer
from .models import Scheduler, Services, SchedulerServices


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


class GetAllServices(APIView):
    def get(self, request):
        services = Services.objects.all()
        return Response(data=ServiceSerializer(instance=services), status=status.HTTP_200_OK)


class CreateServiceView(LoginRequiredMixin, APIView):
    def post(self, request):
        scheduler = Scheduler.objects.filter(user=request.user)
        if not scheduler:
            return Response(data={'detail': 'you are not scheduler !!'}, status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        try:
            Services.objects.create(title=data['title'], description=data['description'], created_by=request.user.id)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as exception:
            return Response(data={'error': exception.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class CreateSchedulerServiceView(LoginRequiredMixin, APIView):
    def post(self, request):
        scheduler = Scheduler.objects.filter(user=request.user)
        if not scheduler:
            return Response(data={'detail': 'you are not scheduler !!'}, status=status.HTTP_400_BAD_REQUEST)
        scheduler = scheduler[0]
        data = request.data
        try:
            SchedulerServices.objects.create(
                scheduler=scheduler.id, service=data['service_id'], about_your_service=data['about_your_service'],
                title=data.get('title'), amount=data['amount']
            )
            return Response(status=status.HTTP_201_CREATED)
        except Exception as exception:
            return Response(data={'error': exception.args[0]}, status=status.HTTP_400_BAD_REQUEST)
