import uuid

from django.conf import settings
from django.db import models

from apps.short_urls.utils import generate_random_string


class ShortUrl(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=settings.RANDOM_STRING_LENGTH,
                                 default=generate_random_string,
                                 unique=True)
