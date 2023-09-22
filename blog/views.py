from django.shortcuts import render

# blog/views.py
from rest_framework import viewsets
from .models import Post, Comment, Tag, Media, Project, ProjectImage
from .serializers import PostSerializer, CommentSerializer, TagSerializer, MediaSerializer, ProjectImageSerializer, ProjectSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class ProjectViewSet(viewSet.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectImageViewSet(viewSet.ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
