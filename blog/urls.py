from rest_framework.routers import DefaultRouter
from .views import TagViewSet, CommentViewSet, PostViewSet, MediaViewSet, ProjectImageViewSet, ProjectViewSet, ProfessionalAchievementListCreate, ProfessionalAchievementDetail, PostsViewSet, ReviewListCreateView, ReviewRetrieveUpdateDestroyView
from django.urls import path


# router = DefaultRouter()
# router.register(r'tags', TagViewSet)
# router.register(r'comments', CommentViewSet)
# router.register(r'posts', PostViewSet)
# router.register(r'media', MediaViewSet)
# router.register(r'project', ProjectViewSet)
# router.register(r'projectimage', ProjectImageViewSet)
# portfolio/urls.py


urlpatterns = [
    path('achievements/', ProfessionalAchievementListCreate.as_view(),
         name='achievement-list'),
    path('achievements/<int:pk>/',
         ProfessionalAchievementDetail.as_view(), name='achievement-detail'),
    path('tags/', TagViewSet.as_view(), name='tags'),
    path('comments/', CommentViewSet.as_view(), name='comments'),
    path('posts/', PostViewSet.as_view(), name='posts'),
    path('post/<int:pk>/', PostsViewSet.as_view(), name='post'),
    path('media/', MediaViewSet.as_view(), name='media'),
    path('projects/', ProjectViewSet.as_view(), name='projects'),
    path('projectimages/', ProjectImageViewSet.as_view(), name='projectimage'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(),
         name='review-detail'),

]
