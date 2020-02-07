from django.db import models
import string as str
from random import choice

# Create your models here.


def generate_id():
    n = 8
    random = str.ascii_uppercase + str.ascii_lowercase + str.digits + '_'
    return ''.join(choice(random) for _ in range(n))


class EventManager(models.Manager):
    def create_event(self, title, location, description, genre, held_date, start_timings, end_timings):
        event = self.model(
            title=title,
            location=location,
            description=description,
            genre=genre,
            held_date=held_date,
            start_timings=start_timings,
            end_timings=end_timings,
        )
        event.save(using=self._db)
        return event


class Event(models.Model):
    title = models.CharField(default='Developers Conference', max_length=500, blank=False)
    slug = models.SlugField(unique=True, max_length=25, default=generate_id)
    location = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    genre = models.CharField(default='Company Development', max_length=255, blank=False, null=False)
    held_date = models.DateField()
    start_timings = models.TimeField()
    end_timings = models.TimeField()

    objects = EventManager()

    REQUIRED_FIELDS = ['title', 'genre', 'location', 'held_date', 'start_timings', 'end_timings']

    def __str__(self):
        return self.title
