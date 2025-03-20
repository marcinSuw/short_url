from django.shortcuts import get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.mixins import CreateModelMixin

from apps.short_urls.models import ShortUrl
from apps.short_urls.serializers import ShortUrlSerializer


class ShorterUrlViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer


@api_view(['GET'])
def redirect_to_long_url(request, short_url):
    url_entry = get_object_or_404(ShortUrl, short_url=short_url)
    return redirect(url_entry.original_url)
