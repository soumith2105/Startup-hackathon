from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework import permissions
from .serializers import (
    EventSerializer,
    EventCreateSerializer,
    EventUpdateSerializer,
)
import datetime
from events.models import Event


class EventListAPIView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        current_time = datetime.datetime.now().time()
        qs = Event.objects.filter(end_timings__gte=current_time)
        return qs

    class Meta:
        model = Event


class EventDetailAPIView(RetrieveAPIView):
    serializer_class = EventSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Event.objects.all()

    class Meta:
        model = Event


class EventCreateAPIView(CreateAPIView):
    serializer_class = EventCreateSerializer
    queryset = Event.objects.all()

    class Meta:
        model = Event


class EventUpdateAPIView(UpdateAPIView):
    serializer_class = EventUpdateSerializer
    lookup_field = 'slug'
    queryset = Event.objects.all()

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
