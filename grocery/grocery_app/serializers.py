from rest_framework import serializers
from .models import Groceries


class GrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Groceries
        fields = "__all__"
