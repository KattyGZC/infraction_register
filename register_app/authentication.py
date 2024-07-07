from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.exceptions import AuthenticationFailed
from .models import Officers

class OfficersJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            officer_id = validated_token['user_id']
        except KeyError:
            raise InvalidToken('Token inválido: no se encontró el NUI del oficial.')

        try:
            officer = Officers.objects.get(id=officer_id)
        except Officers.DoesNotExist:
            raise AuthenticationFailed('Oficial de tránsito no encontrado.')

        return officer
