from django.shortcuts import render
from .models import item, Funcionarios, TimeDeFutebol
from .serializers import ItemSerializers, FuncionariosSerializer, TimeDeFutebolSerializer
from rest_framework import viewsets

class ItemViewSet(viewsets.ModelViewSet):
    queryset = item.objects.all()
    serializer_class = ItemSerializers
    
# Create your views here.

class FuncionariosViewSet(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer


class TimeDeFutebolViewSet(viewsets.ModelViewSet):
    queryset = TimeDeFutebol.objects.all()
    serializer_class = TimeDeFutebolSerializer