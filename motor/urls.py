from django.urls import path
from . import views

urlpatterns = [
    path('escanear/', views.scanner_engine, name='scanner_engine'),
]