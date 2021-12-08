from rest_framework import generics

from auth_example.models.user import User
from auth_example.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class UserUpdateView(generics.UpdateAPIView): # Agregando update al nom,bre de la clase y función de generics se tiene este CRUD
    queryset = User.objects.all() # Si ha más modelos se cambia el User
    serializer_class = UserSerializer  # Y se cambia el serializer por el modelo que se quierea para el update. Igual con delete
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class UserDeleteView(generics.DestroyAPIView): # Agregando delete al nom,bre de la clase y destroy a la función de generics se tiene este CRUD
    queryset = User.objects.all()  
    serializer_class = UserSerializer  
    def delete(self, request, *args, **kwargs): # se pone delete en el método y destroy en la función de la super clase en la sig. línea de cod
        return super().destroy(request, *args, **kwargs)

        # los otros CRUD son ListAPIView y CreateAPIVIew