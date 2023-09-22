# api/urls.py
from rest_framework.routers import DefaultRouter
from .views import TagViewSet, CommentViewSet, PostViewSet, MediaViewSet, ProjectImageViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'posts', PostViewSet)
router.register(r'media', MediaViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'projectimage', ProjectImageViewSet)

urlpatterns = router.urls
