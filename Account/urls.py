from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, RightViewSet, RoleViewSet, MenuViewSet, CategoryViewSet, CategoryLevelView

route = routers.DefaultRouter()
route.register(r'user', UserViewSet, basename='user')
route.register(r'right', RightViewSet, basename='right')
route.register(r'role', RoleViewSet, basename='role')
route.register(r'menu', MenuViewSet, basename='menu')
route.register(r'category', CategoryViewSet, basename='category')
route.register(r'cate', CategoryLevelView, basename='cate')


urlpatterns = [
    path('', include(route.urls))
]
