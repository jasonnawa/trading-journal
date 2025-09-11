from django.urls import path, include
from rest_framework.routers import DefaultRouter
from journal.views import StrategyViewSet


router = DefaultRouter()
router.register(r'strategys', StrategyViewSet, basename='strategy')

urlpatterns = [
    path('', include(router.urls)),
]