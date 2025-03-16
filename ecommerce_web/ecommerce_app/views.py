from django.shortcuts import render
from rest_framework import viewsets
from .models import AccountInfo, Address
from .serialize import AccountInfoSerialize, AddressSerialize
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView


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


# alternative method to mixins

# class AddressView(APIView):
#     def get(self, request):
#         address = Address.objects.all()
#         serialize = AddressSerialize(address, many=True)
#         return Response(serialize.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serialize = AddressSerialize(data=request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data, status=status.HTTP_201_CREATED)
#         return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


# class SingleAddress(APIView):

#     def get_object(self, id):
#         try:
#             return Address.objects.get(pk=id)
#         except Address.DoesNotExist:
#             return None

#     def get(self, request, id):
#         address = self.get_object(id)
#         if address is not None:
#             try:
#                 account_info = address.id
#             except AccountInfo.DoesNotExist:
#                 return Response(
#                     {"error": "Account information not found"},
#                     status=status.HTTP_404_NOT_FOUND,
#                 )

#             serializer = AddressSerialize(address)  # Use your serializer here
#             return Response(serializer.data)  # Return serialized data
#         return Response(
#             {"error": "Address not found"}, status=status.HTTP_404_NOT_FOUND
#         )


#     def put(self, request, id):
#         address = self.get_object(id)
#         serialize = AddressSerialize(address, data=request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data, status=status.HTTP_200_OK)
#         return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         address = self.get_object(id)
#         address.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class AddressView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Address.objects.all()
    serializer_class = AddressSerialize

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class SingleAddress(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Address.objects.all()
    serializer_class = AddressSerialize

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
