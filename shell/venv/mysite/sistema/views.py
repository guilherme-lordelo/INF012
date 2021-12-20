from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pyrebase import pyrebase
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User, Group
from sistema.serializers import ClienteSerializer, FornecedorSerializer, FuncionarioSerializer, VeiculoSerializer
from .models import  Cliente, Fornecedor, Funcionario, Veiculo
#import pyrebase

# Create your views here.

#from django.http import HttpResponse




class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.AllowAny]

class FornecedorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    permission_classes = [permissions.AllowAny]

class FuncionarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [permissions.AllowAny]

class VeiculoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    permission_classes = [permissions.AllowAny]






config={
  "apiKey": "AIzaSyCCadB_Cl0K7hsbBfx0eVdP3GgeoyokC2o",
  "authDomain": "inf012-14887.firebaseapp.com",
  "databaseURL": "https://inf012-14887-default-rtdb.firebaseio.com/",
  "projectId": "inf012-14887",
  "storageBucket": "inf012-14887.appspot.com",
  "messagingSenderId": "911911664468",
  "appId": "1:911911664468:web:7c5c8a116b09c5d4a3e6c1"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def index(request):
        #accessing our firebase data and storing it in a variable
        name = database.child('Data').child('Name').get().val()
        stack = database.child('Data').child('Stack').get().val()
        framework = database.child('Data').child('Framework').get().val()
    
        context = {
            'name':name,
            'stack':stack,
            'framework':framework
        }
        return render(request, 'index.html', context)


#def index(request):
#    return HttpResponse("Hello, world. You're at the sistema index.")