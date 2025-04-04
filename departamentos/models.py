from django.db import models

class balanco(models.Model):
    id = models.AutoField(primary_key=True)
    descricao_balanco = models.CharField(max_length=1000)
    status = models.BooleanField(default=1)
    constrangimento_descricao = models.CharField(max_length=1000)
    atividade_previsto_descricao = models.CharField(max_length=1000)
    progresso = models.CharField(max_length=10,default="")
    id_acao = models.IntegerField(default=True)
    datecreate = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)

     


