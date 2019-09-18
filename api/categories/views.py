from django.shortcuts import render
from rest_framework import viewsets

from .models import Category
from .serializers import ReadCategorySerializer, CreateCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadCategorySerializer
        elif self.request.method == 'POST':
            return CreateCategorySerializer
