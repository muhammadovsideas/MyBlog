from rest_framework import generics, permissions
from .serializers import *
from .models import *
from users.permissions import IsAdmin,IsUser
from rest_framework.parsers import MultiPartParser, FormParser




class AdminInformationView(generics.ListAPIView):
    serializer_class = AdminSerializer
    queryset = User.objects.filter(role='ADMIN')
    permission_classes = (permissions.AllowAny,)


class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer



class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsUser]
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        return self.request.user

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        return User.objects.all()







