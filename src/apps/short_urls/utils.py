import random
import string

from django.conf import settings


def generate_random_string():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=settings.RANDOM_STRING_LENGTH))
