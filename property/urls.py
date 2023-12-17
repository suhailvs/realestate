
from django.urls import path
from . import views

app_name = "property"
urlpatterns = [
    path('<int:property>/', views.PropertyDetail.as_view(), name='property_detail'),
]
