from rest_framework.serializers import ModelSerializer
from events.models import Event
import datetime


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventCreateSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate_held_date(self, value):
        if value <= datetime.datetime.now().date():
            raise ValueError("Date entered cannot be accepted")
        return value

    def create(self, validated_data):
        title = validated_data.get("title")
        location = validated_data.get("location")
        description = validated_data.get("description")
        genre = validated_data.get("genre")
        held_date = validated_data.get("held_date")
        start_timings = validated_data.get("start_timings")
        end_timings = validated_data.get("end_timings")
        event = Event.objects.create_event(title, location, description, genre, held_date, start_timings, end_timings)
        return event


class EventUpdateSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

    def validate_held_date(self, value):
        if value <= datetime.datetime.now().date():
            raise ValueError("Date entered cannot be accepted")
        return value
