from django.db import models

class balanco_geral(models.Model):
    id = models.AutoField(primary_key=True)
    descricao_balanco = models.CharField(max_length=1000)
    atividade_nao_realizada = models.CharField(max_length=1000)
    field_balanco = models.CharField(max_length=50)
    field_atividade = models.CharField(max_length=50)
    status = models.BooleanField(default=1)
    data_registo = models.CharField(max_length=10,default=True)
    datecreate = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)

