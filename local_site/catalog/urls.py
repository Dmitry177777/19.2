
from django.urls import path
from .views import *
from .apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
     path('', index),
    path('contacts/', contacts),
]