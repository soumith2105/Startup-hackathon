from django.urls import path
from .views import (
    StartupCreateUserAPIView,
    MentorCreateUserAPIView,
    ModifyUserAPIView,
    LoginUserAPIView,
    LogoutUserAPIView,
    ChangePasswordAPIView,
    DetailUserAPIView,
    MentorListAPIView,
)


urlpatterns = [
    path('startupsignup/', StartupCreateUserAPIView.as_view(), name='startup-signup'),
    path('mentorsignup/', MentorCreateUserAPIView.as_view(), name='mentor-signup'),
    path('mentors/', MentorListAPIView.as_view(), name='mentors-list'),
    path('login/', LoginUserAPIView.as_view(), name='login'),
    path('logout/', LogoutUserAPIView.as_view(), name='logout'),
    path('pwdchange/', ChangePasswordAPIView.as_view(), name='change_password'),
    path('<username>/', DetailUserAPIView.as_view(), name='profile-info'),
    path('<username>/edit/', ModifyUserAPIView.as_view(), name='update-info'),
]