from rest_framework import generics, permissions
from .serializers import *
from .models import *
from .permissions import IsAdmin,IsUser




class AdminInformationView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter(role='ADMIN')
    permission_classes = (permissions.AllowAny,)


class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer



class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsUser]

    def get_object(self):
        return self.request.user

class UserRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        return User.objects.all()







