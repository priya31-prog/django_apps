from django.shortcuts import render
from rest_framework import viewsets
from .models import AccountInfo
from .serialize import AccountInfoSerialize


class AccountInfoView(viewsets.ModelViewSet):
    queryset = AccountInfo.objects.all()
    serializer_class = AccountInfoSerialize

    def retrive(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# Create your views here.
