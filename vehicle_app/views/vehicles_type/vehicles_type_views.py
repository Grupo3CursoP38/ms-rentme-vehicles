from rest_framework import viewsets
from vehicle_app.serializers.vehicleTypeSerializer import VehicleTypeSerializer
from vehicle_app.models.vehicle_type import Vehicle_type


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = Vehicle_type.objects.all()
    serializer_class = VehicleTypeSerializer
    lookup_field = 'name'
    