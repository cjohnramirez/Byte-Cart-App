from django.contrib.auth.models import User
from user.models import User as UserList
from user.serializers import UserSerializer
from rest_framework import generics, permissions
from user.permissions import IsOwnerOrReadOnly

class UserListCreate(generics.ListCreateAPIView):  # <-- Changed this
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = UserList.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = UserList.objects.all()
    serializer_class = UserSerializer
