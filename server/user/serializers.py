from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'phone_number', 'owner']
