from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db import connection
from .models import balanco
from django.core.serializers import serialize



# Create your views here.
@csrf_exempt
def list_home(request):

     query = '''
                 select ac.id as id,
                 p.descricao as processo,
                 aa.descricao as atividade_anual,
                 aa.data_inicio as data_inicio_as,
                 ac.data_registo as data_registo,
                 ac.descricao as acao,
                 ac.data_fim as data_fim_as,
                 ac.data_inicio as data_inicio_ac,
                 ac.data_fim as data_fim_ac,
                 ac.id_processo as id_processo,
                 ac.id_processo as id_processo,
                 ar.descricao as departamento_responsavel,
                 oa.descricao as objetivo_anual
                 from master_acao as ac
                 left join master_atividade_anual as aa on ac.id_atividade_anual=aa.id
                 left join master_processo as p on ac.id_processo=p.id
                 left join master_departamento as dp on ac.id_departamento_responsavel=dp.id
                 left join master_departamento as dp_aux on ac.id_departamento_auxiliar=dp_aux.id
                 left join master_objetivo_anual as oa on aa.id_objetivo_anual=oa.id
                 left join master_departamento as ar on ac.id_departamento_responsavel=ar.id


             '''
     with connection.cursor() as cursor:
          cursor.execute(query)

          colunas = [col[0] for col in cursor.description] 
          resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]

          

          paginator = Paginator(resultados, 7)
          print(paginator)
          page_number = request.GET.get("page")  
          oa = paginator.get_page(page_number)
          
          return render(request, "departamentos/index.html", {"acao":oa}) 

@csrf_exempt
def adicionar_balanco(request):

     if request.method == "POST":
      try:
                    balanco_descricao= request.POST.get("balanco")
                    descricao_descricao = request.POST.get("constrangimento")
                    atividade_previsto = request.POST.get("atividade_previsto")
                    progresso = request.POST.get("progresso")
                    id_acao = request.POST.get("id_acao")
                    
                    validate = balanco.objects.filter(id_acao=id_acao).count()
                    if validate==0:
                         balanco.objects.create(
                                   descricao_balanco=balanco_descricao,
                                   constrangimento_descricao=descricao_descricao,
                                   atividade_previsto_descricao=atividade_previsto,
                                   progresso=progresso,
                                   id_acao=id_acao
                              )
                         message='A balanço registado com sucesso!!'
                         status= 'success'
                    else:
                          bo=get_object_or_404(balanco, id_acao=id_acao)
                          bo.descricao_balanco = balanco_descricao
                          bo.constrangimento_descricao = descricao_descricao
                          bo.atividade_previsto_descricao = atividade_previsto
                          bo.progresso = progresso
                          bo.save()

                          message='A balanço editado com sucesso!!'
                          status= 'success'

                    return JsonResponse({'status':status, 'message': message })

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def editar_balanco(request):

     if request.method == "POST":
      try:
                      id_acao = request.POST.get("id_acao")
                      bl = balanco.objects.filter(id_acao=id_acao)
                                             
                      message='A balanço editado com sucesso!!'
                      status= 'success'

                      return JsonResponse(serialize("json", bl),safe=False)

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)