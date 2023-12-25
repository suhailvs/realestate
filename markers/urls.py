from django.urls import path, include
from rest_framework import routers
from markers.views import MarkersMapView, MarkerViewSet

app_name = "markers"

router = routers.DefaultRouter()
router.register(r"markers", MarkerViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("", MarkersMapView.as_view()),
]
