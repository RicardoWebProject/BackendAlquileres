#Serializadores para los Usuarios / Clientes
from rest_framework import serializers
#Modelo USER para trabajar
from django.contrib.auth.models import User
#Importar el Token de RF
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_staff',)
        extra_kwargs = {'password': {'write_only': True}} #Para no mostrar la contraseña de vuelta
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
            is_staff = validated_data['is_staff'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user = user)
        return user

