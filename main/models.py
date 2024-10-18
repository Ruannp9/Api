from django.db import models

class item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.FloatField()
    
    def __str__(self):
        return self.nome
    
    
class Funcionarios(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    Data_ingresso = models.DateField()
    
    def __str__(self):
        return self.nome
    
    
class TimeDeFutebol(models.Model):
    nome_jogador = models.CharField(max_length=100)
    nome_time = models.CharField(max_length=100)
    Salario = models.IntegerField()
    
def __str__(self):
    return self.nome

    