from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from api_pickup.models import (
    Role,
    Person, 
    Shipment, 
    ShipmentDetails, 
    ShipmentStatus, 
    ShipmentType, 
    PaymentData, 
    PaymentDetails, 
    PaymentType, 
    Product, 
    ProductDetails, 
    ProductType, 
    Stock, 
    StatusCatalog, 
    Locations)
from api_pickup.serializers import (
    GroupSerializer,
    UserSerializer,
    RoleSerializer,
    PersonSerializer, 
    ShipmentSerializer, 
    ShipmentDetailsSerializer, 
    ShipmentStatusSerializer, 
    ShipmentTypeSerializer, 
    PaymentDataSerializer, 
    PaymentDetailsSerializer, 
    PaymentTypeSerializer, 
    ProductSerializer, 
    ProductDetailsSerializer, 
    ProductTypeSerializer, 
    StockSerializer, 
    StatusCatalogSerializer, 
    LocationsSerializer,
    RegisterUserSerializer)

from rest_framework.permissions import IsAuthenticated



class UserListView(generics.ListCreateAPIView):
    """Handles creating and listing Users."""
    queryset = User.objects.all()

def create(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GroupViewSet(viewsets.ViewSet):
    # permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = Group.objects.all()
        serializer_class = GroupSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = GroupSerializer(data=request.data)
        print("serializer class readed")
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ViewSet):
    # permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = User.objects.all()
        serializer_class = UserSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = UserSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


# Roles
class RoleViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = Role.objects.all()
        serializer_class = RoleSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = RoleSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

# Users
class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = Person.objects.all()
        serializer_class = PersonSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = PersonSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class ShipmentTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = ShipmentType.objects.all()
        serializer_class = ShipmentTypeSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = ShipmentTypeSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = PaymentType.objects.all()
        serializer_class = PaymentTypeSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = PaymentTypeSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = ProductType.objects.all()
        serializer_class = ProductTypeSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = ProductTypeSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

# # Shipments
class ShipmentViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = Shipment.objects.all()
        serializer_class = ShipmentSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = ShipmentSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = ProductSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = Locations.objects.all()
        serializer_class = LocationsSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = LocationsSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class StatusCatalogViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = StatusCatalog.objects.all()
        serializer_class = StatusCatalogSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = StatusCatalogSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class ShipmentStatusViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = ShipmentStatus.objects.all()
        serializer_class = ShipmentStatusSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = ShipmentStatusSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class ShipmentDetailsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = ShipmentDetails.objects.all()
        serializer_class = ShipmentDetailsSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = ShipmentDetailsSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


# # Products
class StockViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = Stock.objects.all()
        serializer_class = StockSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = StockSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = ProductDetails.objects.all()
        serializer_class = ProductDetailsSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = ProductDetailsSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)



# # Payments
class PaymentDataViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = PaymentData.objects.all()
        serializer_class = PaymentDataSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = PaymentDataSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetailsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = PaymentDetails.objects.all()
        serializer_class = PaymentDetailsSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = PaymentDetailsSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
