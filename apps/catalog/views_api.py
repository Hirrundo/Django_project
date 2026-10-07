from rest_framework import viewsets
from .models import Category, Dish
from .serializers import CategorySerializer, DishSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Категории: только чтение.
    list: GET /api/categories/
    retrieve: GET /api/categories/<slug>/
    """
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class DishViewSet(viewsets.ModelViewSet):
    """Блюда: полный CRUD.
    list: GET /api/dishes/
    create: POST /api/dishes/
    retrieve: GET /api/dishes/<slug>/
    update: PUT /api/dishes/<slug>/
    partial: PATCH /api/dishes/<slug>/
    delete: DELETE /api/dishes/<slug>/
    """
    queryset = Dish.objects.filter(is_available=True).select_related('category')
    serializer_class = DishSerializer
    lookup_field = 'slug'