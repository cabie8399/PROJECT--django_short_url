from rest_framework import serializers
from shortUrl.models import ShortUrl

class ShortUrlSerializer(serializers.Serializer):
    
    url = serializers.CharField()
    
    
    class Meta:
        ref_name = 'short_url'