from django.db import models
from .user import User # El punto es para buscar en la misma carpeta y luego la clase User de del archivo user.py

class Account(models.Model): #Importación genérica
    id               = models.AutoField(primary_key=True)
    user             = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE) # Se asocia a la clase User. En User la PK es user, por lo tanto acá es FK
                        # los related_name debe ser únicos en todo el proyrcto. On_delete es para borrar todas las cuentas de ese usuario
    balance          = models.IntegerField(default=0)
    last_change_date = models.DateTimeField()
    is_active        = models.BooleanField(default=True)
