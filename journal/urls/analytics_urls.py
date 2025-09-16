from rest_framework.routers import DefaultRouter
from journal.views.analytics.analytics_view import AnalyticsViewSet

router = DefaultRouter()
router.register(r'analytics', AnalyticsViewSet, basename='analytics')

urlpatterns = router.urls
