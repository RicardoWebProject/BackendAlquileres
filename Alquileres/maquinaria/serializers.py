#Serializadores de Maquinaria
from rest_framework import serializers
#Modelos
from .models import Maquinaria

class MaquinariaSerializer(serializers.ModelSerializer):
    # tipo = serializers.SerializerMethodField()
    
    class Meta:
        model = Maquinaria
        fields = '__all__'
        
    # def get_tipo(self, obj):
    #     return obj.get_tipo_display()