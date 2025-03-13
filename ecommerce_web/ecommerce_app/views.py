from django.shortcuts import render
from rest_framework import viewsets
from .models import AccountInfo
from .serialize import AccountInfoSerialize
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# class AccountInfoView(viewsets.ModelViewSet):
#     queryset = AccountInfo.objects.all()
#     serializer_class = AccountInfoSerialize


#     def retrive(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)


@api_view(["GET", "POST"])
def AccountInfoView(request):
    if request.method == "GET":
        queryset = AccountInfo.objects.all()
        serializer = AccountInfoSerialize(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = AccountInfoSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def SingleAccountView(request, id):
    try:
        queryset = AccountInfo.objects.get(pk=id)
    except AccountInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AccountInfoSerialize(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = AccountInfoSerialize(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
