from django.contrib.auth.models import User, Group
from rest_framework import viewsets
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


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Roles
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

# Users
class PersonViewSet(viewsets.ModelViewSet):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer    


class ShipmentTypeViewSet(viewsets.ModelViewSet):
    queryset = ShipmentType.objects.all()
    serializer_class = ShipmentTypeSerializer

class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

# # Shipments
class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer


class StatusCatalogViewSet(viewsets.ModelViewSet):
    queryset = StatusCatalog.objects.all()
    serializer_class = StatusCatalogSerializer


class ShipmentStatusViewSet(viewsets.ModelViewSet):
    queryset = ShipmentStatus.objects.all()
    serializer_class = ShipmentStatusSerializer


class ShipmentDetailsViewSet(viewsets.ModelViewSet):
    queryset = ShipmentDetails.objects.all()
    serializer_class = ShipmentDetailsSerializer


# # Products
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class ProductDetailsViewSet(viewsets.ModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer


# # Payments
class PaymentDataViewSet(viewsets.ModelViewSet):
    queryset = PaymentData.objects.all()
    serializer_class = PaymentDataSerializer


class PaymentDetailsViewSet(viewsets.ModelViewSet):
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentDetailsSerializer
