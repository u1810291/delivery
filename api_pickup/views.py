from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
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
    Locations
)
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
    LocationsSerializer

)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
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
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ShipmentTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ShipmentType.objects.all()
    serializer_class = ShipmentTypeSerializer

class PaymentTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LocationsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer


class StatusCatalogViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = StatusCatalog.objects.all()
    serializer_class = StatusCatalogSerializer


class ShipmentStatusViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ShipmentStatus.objects.all()
    serializer_class = ShipmentStatusSerializer


class ShipmentDetailsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ShipmentDetails.objects.all()
    serializer_class = ShipmentDetailsSerializer


# # Products
class StockViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class ProductDetailsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer


# # Payments
class PaymentDataViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = PaymentData.objects.all()
    serializer_class = PaymentDataSerializer


class PaymentDetailsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentDetailsSerializer
