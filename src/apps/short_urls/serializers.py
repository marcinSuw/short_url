from django.conf import settings
from django.db import IntegrityError
from rest_framework import serializers

from apps.short_urls.models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = '__all__'

    def create(self, validated_data):
        obj = ShortUrl.objects.filter(original_url=validated_data['original_url']).first()
        if obj:
            return obj
        # for collision 10 try
        for x in range(settings.MAX_RETRY_ATTEMPTS):
            try:
                return super(ShortUrlSerializer, self).create(validated_data)
            except IntegrityError:
                pass
        raise serializers.ValidationError('Try later')
