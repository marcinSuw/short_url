from django.conf import settings
from django.db import IntegrityError
from rest_framework import serializers

from apps.short_urls.models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = ShortUrl
        fields = ('short_url', 'original_url')
        extra_kwargs = {
            "short_url": {"read_only": True},
            "original_url": {"write_only": True}
        }

    def get_short_url(self, obj):
        return f"{settings.BACKEND_DOMAIN}/{obj.short_url}"

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
