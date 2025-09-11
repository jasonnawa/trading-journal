from django.urls import path, include

urlpatterns = [
    path('', include('journal.urls.user_urls')),
    path('', include('journal.urls.tag_urls')),
    path('', include('journal.urls.strategy_urls'))
]