from rest_framework import serializers
from .models import Infraction, Vehicle

class InfractionSerializer(serializers.ModelSerializer):
    patente = serializers.CharField(write_only=True)
    vehicle = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Infraction
        fields = ['vehicle', 'timestamp', 'comment', 'patente']

    def validate_patente(self, value):
        try:
            vehicle = Vehicle.objects.get(patente=value)
        except Vehicle.DoesNotExist:
            raise serializers.ValidationError("El vehículo con la patente proporcionada no existe.")
        return vehicle

    def create(self, validated_data):
        vehicle = validated_data.pop('patente')
        infraction = Infraction.objects.create(vehicle=vehicle, **validated_data)
        return infraction