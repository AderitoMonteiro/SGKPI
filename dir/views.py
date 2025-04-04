# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.db import connection
from departamentos.models import balanco
from django.http import JsonResponse




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
                 oa.descricao as objetivo_anual,
                 CASE
                    WHEN db.status=1 THEN "fa fa-lock"
                    ELSE "fa fa-unlock" 
                 END as class,
                 CASE
                    WHEN db.status=1 THEN "Bloquear"
                    ELSE "Desbloquear" 
                 END as title
                 from master_acao as ac
                 left join master_atividade_anual as aa on ac.id_atividade_anual=aa.id
                 left join master_processo as p on ac.id_processo=p.id
                 left join master_departamento as dp on ac.id_departamento_responsavel=dp.id
                 left join master_departamento as dp_aux on ac.id_departamento_auxiliar=dp_aux.id
                 left join master_objetivo_anual as oa on aa.id_objetivo_anual=oa.id
                 left join master_departamento as ar on ac.id_departamento_responsavel=ar.id
                 left join departamentos_balanco as db on ac.id=db.id_acao

             '''
     with connection.cursor() as cursor:
          cursor.execute(query)

          colunas = [col[0] for col in cursor.description] 
          resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]

          

          paginator = Paginator(resultados, 7)
          print(resultados)
          page_number = request.GET.get("page")  
          oa = paginator.get_page(page_number)
          
          return render(request, "dir/index.html", {"acao":oa}) 


@csrf_exempt
def mudar_balanço(request):

     if request.method == "POST":
      try:
                      id_acao = request.POST.get("id_acao")
                      bl = get_object_or_404(balanco, id_acao=id_acao)

                      if bl.status==0:
                         bl.status=1
                      else:
                         bl.status=0

                      bl.save()
                                             
                      message='A balanço bloqueado com sucesso!!'
                      status= 'success'

                      return JsonResponse({'status':status, 'message': message })

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

