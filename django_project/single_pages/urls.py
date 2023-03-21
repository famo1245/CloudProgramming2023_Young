# urlconf for single_pages

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
]