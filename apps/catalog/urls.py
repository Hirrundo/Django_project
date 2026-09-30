from django.urls import path
from .views import get_catalog,get_by_id

app_name='catalog'
urlpatterns = [
    path('',get_catalog,name='dish_list'),
    path('<int:id>',get_by_id)
]