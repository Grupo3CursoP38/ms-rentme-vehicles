from rest_framework import status, viewsets
from rest_framework.response import Response

from vehicle_app.serializers.vehicleSerializer import VehicleSerializer
from vehicle_app.models.vehicle import Vehicle


class VehicleViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.request.method == 'DELETE':
            return Vehicle.objects.all()
        else:
            return Vehicle.objects.filter(is_active=True)

    serializer_class = VehicleSerializer


class DeactiveVehicle(viewsets.GenericViewSet):

    queryset = Vehicle.objects.filter(is_active=True)
    serializer_class = VehicleSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)