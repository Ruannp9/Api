from rest_framework import serializers
from .models import item, Funcionarios, TimeDeFutebol

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = item #model sempre deve estar escrito assim.
        fields = [
            'nome','descricao','valor'
        ] 
        
        # fields = ' all '
    

class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios 
        fields = [
            'nome','email','Data_ingresso'
        ] 

class TimeDeFutebolSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeDeFutebol
        fields = [
            'nome_jogador','nome_time','Salario'
        ]
        
