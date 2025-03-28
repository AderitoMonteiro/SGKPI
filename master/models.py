from django.db import models

class objetivo_estrategico(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    datecreate = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)

class rastreabilidade(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    id_tabela_meta = models.IntegerField(default=True)
    datecreate = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)

    


class meta(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    datecreate = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)


