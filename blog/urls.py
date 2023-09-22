# api/urls.py
from rest_framework.routers import DefaultRouter
from .views import TagViewSet, CommentViewSet, PostViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = router.urls
