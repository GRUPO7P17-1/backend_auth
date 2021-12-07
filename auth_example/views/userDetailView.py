from django.conf import settings # acceso al settings del proyecto
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from auth_example.models.user import User
from auth_example.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all() # Traer toda la tabla User 
    serializer_class = UserSerializer  # Para tener acceso al to_representation
    permissison_classes = (IsAuthenticated)

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM']) # del archivo settings
        valid_data = token_backend.decode(token, verify = False)

        if valid_data['user_id'] != kwargs['pk']: # user_id en settings en la variable SIMPLE_JWT para validar que se peude hacer la consulta del mismo usuairo
            StringResponse = {'detail' : 'Acceso no autorizado'}
            return Response(StringResponse, status = status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)