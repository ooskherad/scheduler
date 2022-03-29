from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mobile', 'created_at', 'email', 'date_of_birth', 'password')

    def create(self, validated_data):
        data = validated_data.data
        return User.objects.create_user(mobile=data['mobile'], password=data['password'])
