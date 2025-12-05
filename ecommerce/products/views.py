from rest_framework import viewsets, filters, permissions
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response

User = get_user_model()

class IsAdminOrReadCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['create','update','partial_update','destroy']:
            return request.user and request.user.is_staff
        return True

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadCreate]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name', 'sku', 'description']

    def perform_create(self, serializer):
        # set seller to current user if authenticated
        seller = self.request.user if self.request.user and self.request.user.is_authenticated else None
        serializer.save(seller=seller)

    @action(detail=False, methods=['get'])
    def search(self, request):
        q = request.query_params.get('q')
        category = request.query_params.get('category')
        qs = self.get_queryset()
        if q:
            qs = qs.filter(name__icontains=q)
        if category:
            qs = qs.filter(category__name__iexact=category)
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
