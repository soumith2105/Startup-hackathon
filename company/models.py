from django.db import models
from profiles.models import UserProfile
import string as str
from random import choice

# Create your models here.

def generate_id():
    n = 8
    random = str.ascii_uppercase + str.ascii_lowercase + str.digits + '_'
    return ''.join(choice(random) for _ in range(n))


class Company(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(unique=True, max_length=25, default=generate_id)
    joined_date = models.DateField(auto_now_add=True)
    field = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Partners(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    partner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.company.name}--->{self.partner.username}"
