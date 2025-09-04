from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('admin-inf/',AdminInformationView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view()),
    path('user-crud/',UserRetrieveUpdateDeleteView.as_view()),
    path('users/<int:pk>/',UserRetrieveDeleteView.as_view()),
    path('user-list/',UserListView.as_view()),
]