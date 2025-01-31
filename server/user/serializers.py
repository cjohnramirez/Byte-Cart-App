from rest_framework import serializers
from user.models import User as UserList
from django.contrib.auth.models import User as AuthUser

class UserSerializer(serializers.ModelSerializer):
  user = serializers.PrimaryKeyRelatedField(
    many=True,  
    queryset=UserList.objects.all()
  )
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    model = UserList
    fields = ['id', 'username', 'user', 'owner']