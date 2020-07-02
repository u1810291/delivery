from rest_framework import routers
from api_pickup import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'roles', views.RoleViewSet, basename='roles')
router.register(r'groups', views.GroupViewSet)
router.register(r'person', views.PersonViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'shipment', views.ShipmentViewSet, basename='shipment')
router.register(r'locations', views.LocationsViewSet)
router.register(r'payment-type', views.PaymentTypeViewSet)
router.register(r'payment-data', views.PaymentDataViewSet)
router.register(r'shipment-type', views.ShipmentTypeViewSet)
router.register(r'status-catalog', views.StatusCatalogViewSet)
router.register(r'shipment-status', views.ShipmentStatusViewSet)
router.register(r'payment-details', views.PaymentDetailsViewSet)
router.register(r'shipment-details', views.ShipmentDetailsViewSet)
