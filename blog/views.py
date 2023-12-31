from django.shortcuts import render
from rest_framework import generics
from .models import ProfessionalAchievement
from .serializers import ProfessionalAchievementSerializer
from rest_framework import viewsets
from .models import Post, Comment, Tag, Media, Project, ProjectImage, Review, ContactProfile
from .serializers import PostSerializer, CommentSerializer, TagSerializer, MediaSerializer, ProjectImageSerializer, ProjectSerializer, ReviewSerializer, ContactProfileSerializer


class TagViewSet(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentViewSet(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ContactViewSet(generics.ListCreateAPIView):
    queryset = ContactProfile.objects.all()
    serializer_class = ContactProfileSerializer


class PostViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PostsViewSet(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class MediaViewSet(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class ProjectViewSet(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class ProjectImageViewSet(generics.ListCreateAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer


class ProfessionalAchievementListCreate(generics.ListCreateAPIView):
    queryset = ProfessionalAchievement.objects.all()
    serializer_class = ProfessionalAchievementSerializer

    action_dict = {
        'get': 'list',
        'post': 'create',
    }


class ProfessionalAchievementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfessionalAchievement.objects.all()
    serializer_class = ProfessionalAchievementSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
