from rest_framework import serializers
from .models import AccountInfo


class AccountInfoSerialize(serializers.ModelSerializer):
    class Meta:
        model = AccountInfo
        fields = "__all__"
