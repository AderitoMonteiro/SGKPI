# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.db import connection
from departamentos.models import balanco
from master.models import data_registo
from .models import balanco_geral
from django.http import JsonResponse
from django.core.serializers import serialize






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
                           WHEN db.status=1 THEN "fa fa-unlock"
                           ELSE "fa fa-lock" 
                        END as class,
                        CASE
                           WHEN db.status=1 THEN "Bloquear"
                           ELSE "Desbloquear" 
                        END as title,
                        CASE
                           WHEN db.status=1 THEN "#blockEmployeeModal"
                           ELSE "#unblockEmployeeModal" 
                        END as action,
                        db.status
                        from master_acao as ac
                        left join master_atividade_anual as aa on ac.id_atividade_anual=aa.id
                        left join master_processo as p on ac.id_processo=p.id
                        left join master_departamento as dp on ac.id_departamento_responsavel=dp.id
                        left join master_departamento as dp_aux on ac.id_departamento_auxiliar=dp_aux.id
                        left join master_objetivo_anual as oa on aa.id_objetivo_anual=oa.id
                        left join master_departamento as ar on ac.id_departamento_responsavel=ar.id
                        left join departamentos_balanco as db on ac.id=db.id_acao

                     '''
         data_rg = '''
                             select 
                              dr.id,
                              dr.descricao
                              from master_data_registo as dr
                              where dr.id not in(
                                 SELECT 
                                 data_registo
                                 FROM dir_balanco_geral WHERE YEAR(datecreate)=YEAR(NOW())
                              )
                  '''
         with connection.cursor() as cursor:
                        cursor.execute(query)

                        colunas = [col[0] for col in cursor.description] 
                        resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]

         with connection.cursor() as cursor:
                        cursor.execute(data_rg)

                        colunas = [col[0] for col in cursor.description] 
                        dateRegisto = [dict(zip(colunas, row)) for row in cursor.fetchall()]


                        paginator = Paginator(resultados, 7)
                        page_number = request.GET.get("page")  
                        oa = paginator.get_page(page_number)
          
                        return render(request, "dir/index.html", {"acao":oa,"data_registo":dateRegisto}) 


@csrf_exempt
def mudar_balanço(request):

     if request.method == "POST":
      try:
                      id_acao = request.POST.get("id_acao")
                      bl = get_object_or_404(balanco, id_acao=id_acao)

                      if bl.status==0:
                         bl.status=1
                         message='A balanço desbloqueada com sucesso!!'
                         status= 'success'
                         bl.save()


                      else:
                         bl.status=0
                         message='A balanço bloqueada com sucesso!!'
                         status= 'success'
                         bl.save()

                      return JsonResponse({'status':status, 'message': message })

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def bloquear_balanco(request):

     if request.method == "POST":
      try:
                       data_registo = request.POST.get("id_data_registo")

                       if data_registo !="":
                              balanco_validate = '''
                                                UPDATE 
                                                departamentos_balanco 
                                                SET status=0 WHERE id_data_registo=%s
                                                
                                       '''

                              with connection.cursor() as cursor:
                                                         cursor.execute(balanco_validate,[data_registo])

                              message='Balanço bloqueada com sucesso!!'
                              status= 'success'

                              return JsonResponse({'status':status, 'message': message })
                       else:
                           message='Erro, tem que selecionar a data de registo!!'
                           status= 'erro'

                           return JsonResponse({'status':status, 'message': message })


      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def balanco_g(request):

     if request.method == "POST":
      try:
                    balanco_descricao= request.POST.get("balanco")
                    atividade_nao_realizada= request.POST.get("atividade_n_realizada")
                    data_registo = request.POST.get("data_registo")
                    field_1= request.POST.get("field_1")
                    field_2 = request.POST.get("field_2")

                    if balanco_descricao !="" and data_registo != "":

                              balanco_validate = '''
                                          SELECT COUNT(*) as count 
                                          FROM departamentos_balanco 
                                          WHERE id_data_registo=%s
                                       
                              '''

                              with connection.cursor() as cursor:
                                          cursor.execute(balanco_validate,[data_registo])
                                          colunas = [col[0] for col in cursor.description] 
                                          validate = [dict(zip(colunas, row)) for row in cursor.fetchall()]
                              
                                          print(validate)
                                          if validate[0]['count']!=0:
                                                         balanco_aberto = '''
                                                                     SELECT COUNT(*) as count 
                                                                     FROM departamentos_balanco 
                                                                     WHERE id_data_registo=%s and status=%s
                                                                  
                                                         '''
                                                         with connection.cursor() as cursor:
                                                                     cursor.execute(balanco_aberto,[data_registo,1])
                                                                     colunas = [col[0] for col in cursor.description] 
                                                                     resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]


                                                         if resultados[0]['count']==0:
                                                                  balanco_geral.objects.create(
                                                                                 descricao_balanco=balanco_descricao,
                                                                                 atividade_nao_realizada=atividade_nao_realizada,
                                                                                 data_registo=data_registo,
                                                                                 field_balanco=field_1,
                                                                                 field_atividade=field_2
                                                                              )
                                                                  message='A balanço geral registado com sucesso!!'
                                                                  status= 'success'
                                                         else:
                                                                  message='Erro, a ainda balanço que não foi bloqueada!!'
                                                                  status= 'error'
                                          else:
                                                   message='Erro, data resgisto invalido!!'
                                                   status= 'error'

                              return JsonResponse({'status':status, 'message': message })
                    else:
                           message='Erro, tem que preencher todos os campos obrigatorios!!'
                           status= 'error'

                           return JsonResponse({'status':status, 'message': message })

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@csrf_exempt
def list_balanco_geral(request):

         query = '''
                        SELECT 
                        dir_balanco_geral.id as id,
                        descricao_balanco,
                        atividade_nao_realizada,
                        field_balanco,
                        field_atividade,
                        master_data_registo.descricao data_registo
                        FROM dir_balanco_geral
                        left join master_data_registo on dir_balanco_geral.data_registo=master_data_registo.id

                     '''
         data_rg = '''
                             select 
                              dr.id,
                              dr.descricao
                              from master_data_registo as dr
                              
                  '''
         with connection.cursor() as cursor:
                        cursor.execute(query)

                        colunas = [col[0] for col in cursor.description] 
                        resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]

         with connection.cursor() as cursor:
                        cursor.execute(data_rg)

                        colunas = [col[0] for col in cursor.description] 
                        dateRegisto = [dict(zip(colunas, row)) for row in cursor.fetchall()]


                        paginator = Paginator(resultados, 7)
                        page_number = request.GET.get("page")  
                        oa = paginator.get_page(page_number)
          
                        return render(request, "bg/index.html", {"dir_balanco_geral":oa,"data_registo":dateRegisto}) 


@csrf_exempt
def ver_balanco_geral(request):

     if request.method == "POST":
      try:
                      id_balanco_geral = request.POST.get("id_balanco_geral")
                      bl = balanco_geral.objects.filter(id=id_balanco_geral)
                   

                      return JsonResponse(serialize("json", bl),safe=False)

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def edit_balanço_geral(request):

     if request.method == "POST":
      try:
                      balanco = request.POST.get("balanco")
                      atividade_n_previsto = request.POST.get("atividade_n_previsto")
                      id_bl_geral = request.POST.get("id_bl_geral")

                      if balanco !="" and atividade_n_previsto !="":
                                 bl = get_object_or_404(balanco_geral, id=id_bl_geral)

                                 bl.descricao_balanco=balanco
                                 bl.field_balanco=request.POST.get("field_1")
                                 bl.field_atividade=request.POST.get("field_2")
                                 bl.atividade_nao_realizada=atividade_n_previsto
                                 bl.save()

                                 message='A balanço alterado com sucesso!!'
                                 status= 'success'

                                 return JsonResponse({'status':status, 'message': message })
                      else:
                           message='Erro, tem que preencher todos os campos obrigatorios!!'
                           status= 'error'

                           return JsonResponse({'status':status, 'message': message })


      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)




