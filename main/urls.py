from django.urls import path

from main.views import *


urlpatterns = [
    path('skills-list/', SkillListView.as_view(), name='skills-list'),
    path('softskills-list/', SoftSkillListView.as_view(), name='softskills-list'),
    path('blogpost-list/', BlogPostListView.as_view(), name='blogpost-list'),
    path('blogpost-detail/<slug:slug>', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('experience-list/', ExperienceListView.as_view(), name='experience-list'),
    path('education-list/', EducationListView.as_view(), name='education-list'),
    path('tag-list/', TagListView.as_view(), name='tag-list'),
    path('chat-create/', ChatCreateView.as_view(), name='chat-create'),
    path('chat-list/', ChatListView.as_view(), name='chat-list'),
    path('chat-delete/<int:pk>/', ChatDeleteView.as_view(), name='chat-delete'),
    path('page-view-log/', PageViewLogListView.as_view(), name='page-view-log'),
]