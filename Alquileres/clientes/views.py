# Create your views here.
#Vistas para los Clientes / Usuarios

#Vistas Genéricas, para simplificar la carga de código y trabajo
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
#Response
from rest_framework.response import Response
#Autenticación
from rest_framework.permissions import IsAuthenticated, IsAdminUser #también está aquí
from django.contrib.auth import authenticate
#Serializador
from .serializers import UserSerializer
#Modelo
from django.contrib.auth.models import User

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()

class LoginView(APIView):
    permission_classes = ()
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username = username, password = password)
        
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Credenciales no válidas.'}, status = status.HTTP_400_BAD_REQUEST)
