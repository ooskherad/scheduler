import re

from rest_framework import serializers
from .models import Scheduler, Services


class SchedulerSerializer(serializers.ModelSerializer):
    user_id = serializers.models

    class Meta:
        model = Scheduler
        fields = ('user_id', 'title', 'secondary_mobile', 'about_you')

    def update(self, instance, validated_data):
        pass

    def validate_secondary_mobile(self, mobile):
        valid_mobile = re.search("^09\d{9}$", mobile)
        if not valid_mobile:
            raise serializers.ValidationError('phone number must start with 09 and must have 11 digits')
        return mobile


class ServiceSerializer(serializers.Serializer):
    class Meta:
        model = Services
        fields = ('__all__',)
