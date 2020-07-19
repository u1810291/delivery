from django.contrib.auth.models import User, Group
from rest_framework import serializers
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


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'



# Roles
class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields = '__all__'


# Users
class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer
    role = RoleSerializer
    class Meta:
        model = Person
        fields = '__all__'
    


class ShipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentType
        fields = '__all__'


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__' 


# # Shipments
class ShipmentSerializer(serializers.ModelSerializer):
    client_id = UserSerializer 
    shipment_type = ShipmentTypeSerializer
    payment_type = PaymentTypeSerializer
    product_type = ProductTypeSerializer
    class Meta:
        model = Shipment
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    product_type_id = ProductTypeSerializer
    class Meta:
        model = Product
        fields = '__all__'


class LocationsSerializer(serializers.ModelSerializer):
    shipment_id = ShipmentSerializer
    user_id = UserSerializer
    product_id = ProductSerializer
    class Meta:
        model = Locations
        fields = '__all__'


class StatusCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusCatalog
        fields = '__all__'


class ShipmentStatusSerializer(serializers.ModelSerializer):
    shipment_id = ShipmentSerializer
    status_catalog = StatusCatalogSerializer
    class Meta:
        model = ShipmentStatus
        fields = '__all__'


class ShipmentDetailsSerializer(serializers.ModelSerializer):
    shipment_id = ShipmentSerializer
    product_id = ProductSerializer
    class Meta:
        model = ShipmentDetails
        fields = '__all__'


# # Products
class StockSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer
    class Meta:
        model = Stock
        fields = '__all__'


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'


# # Payments
class PaymentDataSerializer(serializers.ModelSerializer):
    payment_type = PaymentTypeSerializer
    class Meta:
        model = PaymentData
        fields = '__all__'


class PaymentDetailsSerializer(serializers.ModelSerializer):
    shipment_id = ShipmentSerializer
    payment_data = PaymentDataSerializer
    class Meta:
        model = PaymentDetails
        fields = '__all__'
