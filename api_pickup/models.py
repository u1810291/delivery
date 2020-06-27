from django.db import models
from django.contrib.auth.models import User


# Roles
class Role(models.Model):
    role = models.IntegerField()
    role_name = models.CharField(max_length=50)


# Users
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.OneToOneField(Role, on_delete=models.CASCADE, default=10)
    country = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=50, null=True)
    user_longitude = models.DecimalField(decimal_places=9, max_digits=20)
    user_latitude = models.DecimalField(decimal_places=9, max_digits=20)


class ShipmentType(models.Model):
    type_name = models.CharField(max_length=255)


class PaymentType(models.Model):
    type_name = models.CharField(max_length=250)


class ProductType(models.Model):
    type_name = models.CharField(max_length=200)


# Shipments
class Shipment(models.Model):
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    shipment_type = models.ForeignKey(ShipmentType, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    time_created = models.DateTimeField()
    shipping_address = models.CharField(max_length=250)
    billing_address = models.CharField(max_length=250)
    delivery_cost = models.DecimalField(decimal_places=9, max_digits=20)
    discount = models.DecimalField(decimal_places=9, max_digits=20)
    final_price = models.DecimalField(decimal_places=9, max_digits=20)
    shipment_longitude = models.DecimalField(decimal_places=9, max_digits=20)
    shipment_latitude = models.DecimalField(decimal_places=9, max_digits=20)




class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255)
    product_type_id = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    unit = models.CharField(max_length=50)
    price_per_unit = models.DecimalField(decimal_places=9, max_digits=20)


class Locations(models.Model):
    shipment_id = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    driver_id = models.IntegerField()
    user_long = models.DecimalField(decimal_places=9, max_digits=20)
    user_lat = models.DecimalField(decimal_places=9, max_digits=20)
    product_long = models.DecimalField(decimal_places=9, max_digits=20)
    product_lat = models.DecimalField(decimal_places=9, max_digits=20)
    driver_long = models.DecimalField(decimal_places=9, max_digits=20)
    driver_lat = models.DecimalField(decimal_places=9, max_digits=20)
    shipping_long = models.DecimalField(decimal_places=9, max_digits=20)
    shipping_lat = models.DecimalField(decimal_places=9, max_digits=20)
    date_create = models.DateTimeField()


class StatusCatalog(models.Model):
    status_name = models.CharField(max_length=255)


class ShipmentStatus(models.Model):
    shipment_id = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    status_catalog = models.ForeignKey(StatusCatalog, on_delete=models.CASCADE)
    status_time = models.DateTimeField()
    notes = models.TextField()


class ShipmentDetails(models.Model):
    shipment_id = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=9, max_digits=20)
    price_per_unit = models.DecimalField(decimal_places=9, max_digits=20)
    price = models.DecimalField(decimal_places=9, max_digits=20)


# Products
class Stock(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, primary_key=True)
    in_stock = models.DecimalField(decimal_places=9, max_digits=20)
    last_update = models.DateTimeField()


class ProductDetails(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200)
    type_name = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    price_per_unit = models.DecimalField(decimal_places=9, max_digits=20)
    in_stock = models.DecimalField(decimal_places=9, max_digits=20)
    product_longitude = models.DecimalField(decimal_places=9, max_digits=20)
    product_latitude = models.DecimalField(decimal_places=9, max_digits=20)
    last_update = models.DateTimeField()


# Payments
class PaymentData(models.Model):
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    data_name = models.CharField(max_length=255)
    data_type = models.CharField(max_length=255)
    date_payed = models.DateTimeField()


class PaymentDetails(models.Model):
    shipment_id = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    payment_data = models.ForeignKey(PaymentData, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)


