# blog/serializers.py
from rest_framework import serializers
from .models import Post, Comment, Tag, Media, Project, ProjectImage, ProfessionalAchievement, Review


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'


class ProfessionalAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalAchievement
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
