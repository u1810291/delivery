from rest_framework import routers
from api_pickup import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'roles', views.RoleViewSet, basename='roles')
router.register(r'groups', views.GroupViewSet, basename='groups')
router.register(r'person', views.PersonViewSet, basename='person')
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'shipment', views.ShipmentViewSet, basename='shipment')
router.register(r'locations', views.LocationsViewSet, basename='locations')
router.register(r'payment-type', views.PaymentTypeViewSet, basename='payment-type')
router.register(r'payment-data', views.PaymentDataViewSet, basename='payment-data')
router.register(r'shipment-type', views.ShipmentTypeViewSet, basename='shipment-type')
router.register(r'status-catalog', views.StatusCatalogViewSet, basename='status-catalog')
router.register(r'shipment-status', views.ShipmentStatusViewSet, basename='shipment-status')
router.register(r'payment-details', views.PaymentDetailsViewSet, basename='payment-details')
router.register(r'shipment-details', views.ShipmentDetailsViewSet, basename='shipment-details')
