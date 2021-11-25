from ..models.vehicle_type import Vehicle_type
from rest_framework import serializers

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_type
        fields = '__all__'