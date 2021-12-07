from rest_framework import serializers
from auth_example.models.account import Account
from auth_example.models.user import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta: # Metadata del serializer
        model = Account
        fields = ['balance', 'last_change_date', 'is_active']

    def to_representaiton(self, obj): # obj es tipo User
        account = Account.objects.get(id=obj.id)
        user = User.objects.get(id=obj.user_id) # user_id porque así aparece en la base de datos la FK en la tabla de account
        return {
            'id' : account.id,
            'balance' : account.balance,
            'last_change_date': account.last_change_date,
            'is_active' : account.is_active,
            'user': {
                'id' : user.id,
                'name' : user.name,
                'email' : user.email
            }
        }
