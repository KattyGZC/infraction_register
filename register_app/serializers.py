from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Infraction, Vehicle, Officers

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
    

class TokenObtainSerializer(serializers.Serializer):
    identification = serializers.IntegerField()

    def validate(self, attrs):
        identification = attrs.get('identification')
        try:
            officer = Officers.objects.get(nui=identification)
        except Officers.DoesNotExist:
            raise serializers.ValidationError({"general_errors": "Oficial de tránsito no encontrado"})

        refresh = RefreshToken.for_user(officer)
        refresh['user_id'] = officer.id
        return {
            'officer': officer.name, 
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }