from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MahsulotViewSet, SavatViewSet

router = DefaultRouter()
router.register(r'mahsulotlar', MahsulotViewSet)
router.register(r'savatlar', SavatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('mahsulotlar/<int:pk>/detail/', MahsulotViewSet.as_view({'get': 'detail'}), name='mahsulot-detail'),
    path('savatlar/<int:pk>/detail/', SavatViewSet.as_view({'get': 'detail'}), name='savat-detail'),
]
