from rest_framework import serializers
from ..models import Image, Comment

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('image', 'name', 'email', 'body',)
