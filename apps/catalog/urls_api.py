from rest_framework.routers import DefaultRouter
from .views_api import CategoryViewSet, DishViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('dishes', DishViewSet, basename='dish')
urlpatterns = router.urls