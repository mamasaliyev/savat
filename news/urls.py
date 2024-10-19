from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, CommentViewSet, NewsDetailView

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('news/<int:pk>/', NewsDetailView.as_view({'get': 'retrieve'}), name='news-detail'),  # Tafsilotlar uchun
]
