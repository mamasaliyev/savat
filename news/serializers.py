from rest_framework import serializers
from .models import News, Comment

class NewsSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'image' ,'description', 'likes', 'comments', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(default='Anonymous', read_only=True)  # Anonim foydalanuvchi

    class Meta:
        model = Comment
        fields = ['id', 'news', 'user', 'content', 'created_at']
