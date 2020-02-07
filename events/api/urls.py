from django.urls import path
from .views import (
    EventListAPIView,
    EventDetailAPIView,
    EventCreateAPIView,
    EventUpdateAPIView
)


urlpatterns = [
    path('', EventListAPIView.as_view(), name='events'),
    path('create/', EventCreateAPIView.as_view(), name='event-create'),
    path('<str:slug>/', EventDetailAPIView.as_view(), name='event-detail'),
    path('<str:slug>/update/', EventUpdateAPIView.as_view(), name='event-update'),
]