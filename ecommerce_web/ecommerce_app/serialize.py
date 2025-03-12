from rest_framework import serializers
from .models import AccountInfo


class AccountInfoSerialize(serializers.ModelSerializer):
    user_name = serializers.CharField(source="userName")

    class Meta:
        model = AccountInfo
        fields = [
            "user_name",
            "userid",
            "phoneNumber",
            "profileImage",
            "email",
            "password",
        ]
