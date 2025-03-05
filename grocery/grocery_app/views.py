from django.shortcuts import render
from rest_framework import viewsets
from .models import Groceries
from .serializers import GrocerySerializer

# Create your views here.


class GroceryViewSet(viewsets.ModelViewSet):
    queryset = Groceries.objects.all()
    serializer_class = GrocerySerializer
