from rest_framework import serializers
from .models import AccountInfo, Address


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


class AddressSerialize(serializers.ModelSerializer):
    user_id = serializers.CharField(source="accountInfo_userid")

    class Meta:
        model = Address
        fields = [
            "user_id",
            "streetName",
            "addressLine1",
            "id",
            "pincode",
        ]
