from ..models.vehicle import Vehicle
from ..models.vehicle_type import Vehicle_type
from rest_framework import serializers
from django.core import exceptions


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'short_description', 'long_description',
                  'color', 'img_url', 'type', 'in_use']

    type = serializers.CharField()

    def create(self, validated_data):

        errors = dict()

        try:

            type = validated_data.pop("type")
            print(type)
            type_instance = Vehicle_type.objects.get(name=type)
            vehicle_instance = Vehicle.objects.create(
                **validated_data, type=type_instance)
            return vehicle_instance

        except exceptions.ObjectDoesNotExist as e:

            errors['type_vehicle'] = e

            raise serializers.ValidationError(errors)

    def update(self, instance, validated_data):

        errors = dict()

        try:

            type = validated_data.pop("type", False)
            if(type):
                print(type)
                type_instance = Vehicle_type.objects.get(name=type)
                validated_data["type"] = type_instance

            return super().update(instance, validated_data)

        except exceptions.ObjectDoesNotExist as e:

            errors['type_vehicle'] = e

            raise serializers.ValidationError(errors)
