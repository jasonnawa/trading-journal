from django.urls import path, include
from rest_framework.routers import DefaultRouter
from journal.views.tag_view import TagViewSet


router = DefaultRouter()
router.register(r'tags', TagViewSet, basename='tag')

urlpatterns = [
    path('', include(router.urls)),
]