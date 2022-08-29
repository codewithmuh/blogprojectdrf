from rest_framework import serializers

from . import models
# > This class is a serializer for the Blog model. It will serialize all fields except for the
# created_at and updated_at fields

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Blog
        exclude = ['created_at', 'updated_at']
        
    