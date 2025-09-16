from django.urls import path, include
from rest_framework.routers import DefaultRouter
from journal.views import JournalEntryView


router = DefaultRouter()
router.register(r'journals', JournalEntryView, basename='journal')

urlpatterns = [
    path('', include(router.urls)),
]