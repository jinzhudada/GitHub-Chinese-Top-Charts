
from comments.models import Comment  # 确保从 comments.models 导入

from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Resource, Category
from .serializers import ResourceSerializer, CategorySerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Resource, Category, Like
from .serializers import ResourceSerializer, CategorySerializer, LikeSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# resources/views.py
from comments.models import Comment  # 绝对导入
from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Resource, Category, Like, Favorite
from .serializers import ResourceSerializer, CategorySerializer, LikeSerializer, FavoriteSerializer, CommentSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        data = response.data
        data['likes_count'] = instance.likes.count()
        data['favorites_count'] = instance.favorites.count()
        data['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return Response(data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ResourceListView(generics.ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

@method_decorator(login_required, name='dispatch')
class RecommendedResourcesView(generics.ListAPIView):
    serializer_class = ResourceSerializer

    def get_queryset(self):
        user = self.request.user
        user_categories = Resource.objects.filter(uploader=user).values_list('category', flat=True).distinct()
        recommended_resources = Resource.objects.filter(category__in=user_categories).exclude(uploader=user)
        return recommended_resources

def index(request):
    categories = Category.objects.all()
    return render(request, 'resources/index.html', {'categories': categories})