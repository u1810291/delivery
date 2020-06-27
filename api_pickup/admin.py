from django.contrib import admin
from api_pickup.models import *


admin.site.register(Role)
admin.site.register(Stock)
admin.site.register(Person)
admin.site.register(Product)
admin.site.register(Shipment)
admin.site.register(Locations)
admin.site.register(PaymentData)
admin.site.register(PaymentType)
admin.site.register(ProductType)
admin.site.register(ShipmentType)
admin.site.register(StatusCatalog) 
admin.site.register(ShipmentStatus)
admin.site.register(ProductDetails)
admin.site.register(PaymentDetails)
admin.site.register(ShipmentDetails)
