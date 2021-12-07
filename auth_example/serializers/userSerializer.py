from auth_example.models.user import User
from auth_example.models.account import Account
from rest_framework import serializers
from .accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta: # Metadata del serializer
        model = User # Modelo a asociar el serializer
        fields = ['id', 'username', 'password', 'name', 'email', 'account'] #campos que espero lleguen desde el body en postman

    def create(self, validated_data): # Se crea la primera cuenta por defecto al crear un usuario, por eso en fields se agregó 'account'
        accountData = validated_data.pop('account') # con pop sacamos la info de la cuenta que recibimos desde postman y guardamos solo info del usuario
        user_instance = User.objects.create(**validated_data) # Solo lo que quedó del usuario, sin la info de account
        Account.objects.create(user=user_instance, **accountData) # user es la llave foránea para crear la cuenta y con **accountData complementamos la info de account
        return user_instance

    def to_representation(self, obj): # La respuesta al servicio web para el ususario. Acá se hacen los inner join
        user = User.objects.get(id=obj.id) # obj es de tipo User
        account = Account.objects.get(user=obj.id) # Busca cual cuenta tiene asociada la FK a la PK en el usuario para traer su cuenta
        return {  # La respuesta en el servicio web y lo que se mostrará al consultar por usuario
            'id' : user.id,
            'username' : user.username,
            'name' : user.name,
            'email' : user.email,
            'account' : {
                'id' : account.id,
                'balance' : account.balance,
                'last_change_date': account.last_change_date,
                'is_active' : account.is_active
            }
        }