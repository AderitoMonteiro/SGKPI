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
    id_kpi = models.IntegerField(default=True)
    datecreate = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)


class kpi(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    id_objeto_estrategico = models.IntegerField(default=True)
    datecreate = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)


class objetivo_anual(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    id_kpi = models.IntegerField(default=True)
    datecreate = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)

class atividade_anual(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    data_inicio =  models.DateField(default=True)
    data_fim= models.DateField(default=True)
    id_objetivo_anual = models.IntegerField(default=True)
    datecreate = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)


class processo(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    datecreate = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)
 
class departamento(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    datecreate = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)

class acao(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    data_inicio =  models.DateField(default=True)
    data_fim= models.DateField(default=True)
    id_atividade_anual = models.IntegerField(default=True)
    id_departamento_responsavel = models.IntegerField(default=True)
    responsavel_nome = models.CharField(max_length=100,default=True)
    id_departamento_auxiliar = models.IntegerField(default=True)
    responsavel_auxiliar_nome = models.CharField(max_length=100,default=True)
    data_registo = models.CharField(max_length=10,default=True)
    obs = models.CharField(max_length=500)
    id_processo = models.IntegerField(default=True)
    datecreate = models.DateTimeField(auto_now_add=True)
    dateupdate = models.DateTimeField(auto_now=True)



