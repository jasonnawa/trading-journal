from django.urls import path, include
from rest_framework.routers import DefaultRouter
from journal.views.user_view import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='tag')

urlpatterns = [
    path('', include(router.urls)),
]