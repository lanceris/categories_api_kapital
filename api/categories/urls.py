from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.CategoryViewSet.as_view({'get':'list', 'post': 'create'})),
    path('categories/<int:pk>/', views.CategoryViewSet.as_view({'get':'retrieve'}))
]