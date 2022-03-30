import re

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mobile', 'email', 'date_of_birth', 'password', 'profile_image')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        data = validated_data
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr =='password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    def validate_mobile(self, mobile):
        valid_mobile = re.search("^09\d{9}$", mobile)
        if not valid_mobile:
            raise serializers.ValidationError('phone number must start with 09 and must have 11 digits')
        return mobile

    def validate_password(self, password):
        # todo validate password
        if password is None:
            raise serializers.ValidationError('password validations')
        return password
