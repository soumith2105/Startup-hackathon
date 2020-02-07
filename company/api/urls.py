from django.urls import path
from .views import CompanyDetailAPIView, CompanyUpdateAPIView


urlpatterns = [
    path('<str:slug>/', CompanyDetailAPIView.as_view(), name='company-detail'),
    path('<str:slug>/update/', CompanyUpdateAPIView.as_view(), name='company-update'),
]