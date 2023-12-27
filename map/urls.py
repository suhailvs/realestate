

from django.conf.urls import include
from django.urls import path
from . import views

app_name = "map"
urlpatterns = [
    path("save_property/", views.save_property, name="save_property"),
    path('<int:property>/', views.PropertyDetail.as_view(), name='property_detail'),
]
