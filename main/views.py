from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.shortcuts import render
from main.serializers import *
from main.models import *
from users.permissions import IsAdmin, IsUser
from .permissions import *


class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]


class SoftSkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SoftSkillSerializer
    permission_classes = [AllowAny]


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'


class BlogPostDetailView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ip = self.get_client_ip(request)

        PageViewLog.objects.get_or_create(
            project=instance,
            ip_address=ip,
        )

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [AllowAny]


class EducationListView(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationsSerializer
    permission_classes = [AllowAny]



class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]


class ChatCreateView(generics.CreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAdminIsUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ChatListView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [AllowAny]


class ChatDeleteView(generics.DestroyAPIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAdminIsUser]
    queryset = Chat.objects.all()

    def get_object(self):
        obj = super().get_object()
        user = self.request.user

        # Agar oddiy foydalanuvchi bo'lsa faqat o'ziga tegishli chatni o'chira oladi
        if not user.is_superuser and obj.user != user:
            raise PermissionDenied("Siz faqat o'zingizga tegishli chatni o'chira olasiz.")
        return obj



class PageViewLogListView(generics.ListAPIView):
    queryset = PageViewLog.objects.all()
    serializer_class = PageViewLogSerializer
    permission_classes = [IsAuthenticated]






