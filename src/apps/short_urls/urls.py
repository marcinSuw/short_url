from django.urls import include, path

from apps.short_urls import views

urlpatterns = [
    path('reduce_url/', views.ShorterUrlViewSet.as_view({'post': 'create'})),
    path('<str:short_url>/', views.redirect_to_long_url),
]
