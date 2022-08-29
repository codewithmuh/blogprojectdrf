from rest_framework import serializers

from . import models

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Blog
        exclude = ['created_at', 'updated_at']
        
        #fields =[
        #    'title', 'user','blog_text', 'main_image'
        #]