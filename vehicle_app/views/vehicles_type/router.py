from rest_framework import routers
from vehicle_app.views.vehicles_type.vehicles_type_views import VehicleTypeViewSet

router = routers.SimpleRouter()

router.register(r'vehicles_type', VehicleTypeViewSet, basename="vehicles")


urlpatterns = router.urls
