from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, ResourceViewSet, CategoryViewSet, ResourceListView, RecommendedResourcesView, LikeViewSet, FavoriteViewSet

router = DefaultRouter()
router.register(r'resources', ResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', index, name='index'),
    path('api/resources/', ResourceViewSet.as_view({'get': 'list', 'post': 'create'}), name='resource-list'),
    path('api/categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('api/search/', ResourceListView.as_view(), name='resource-search'),
    path('api/recommended/', RecommendedResourcesView.as_view(), name='recommended-resources'),
    path('api/likes/', LikeViewSet.as_view({'get': 'list', 'post': 'create'}), name='like-list'),
    path('api/favorites/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite-list'),
]
