from rest_framework import routers
from vehicle_app.views.vehicles.vehicles_views import VehicleViewSet, DeactiveVehicle

router = routers.SimpleRouter()

router.register(r'vehicles', VehicleViewSet, basename="vehicles")
router.register(r'deactiveVehicle', DeactiveVehicle, basename="deactiveVehicle")

urlpatterns = router.urls
