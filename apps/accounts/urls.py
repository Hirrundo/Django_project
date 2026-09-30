from django.urls import path
from .views import register_view,LoginView,LogoutView
app_name = 'accounts'
urlpatterns = [
    path('register/',register_view, name='register'),
    path('login/',LoginView.as_view(), name='login')
]