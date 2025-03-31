from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import objetivo_estrategico,rastreabilidade,meta,kpi,objetivo_anual,atividade_anual,acao,processo,departamento
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db import connection



#start modulo objetivo_estrategico

def master_view(request):
     return render(request, "master/GOE/index.html")

@csrf_exempt
def create_objetivo_estrategico(request):

    if request.method == "POST":
      try:
 
                    descricao = request.POST.get("descricao")
                    status = "1"

                    validate = objetivo_estrategico.objects.filter(descricao=descricao).count()

                    if validate==0:
                              objetivo_estrategico.objects.create(
                                   descricao=descricao,
                                   status=status
                              )
                              message='Registo criado com sucesso!'
                              status= 'success'
                    else:
                         message='A descrição inserido ja existe!!'
                         status= 'error'
                    return JsonResponse({'status':status, 'message': message })

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


def list_create_objetivo_estrategico(request):

    oes_list = objetivo_estrategico.objects.all()
    paginator = Paginator(oes_list, 7)

    page_number = request.GET.get("page")  # Obter o número da página da URL
    oes = paginator.get_page(page_number)

    return render(request, "master/GOE/index.html", {"objetivo_estrategico":oes})  

@csrf_exempt
def editar_objetivo_estrategico(request):

     if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_oes= request.POST.get("id")
                    
                    validate = objetivo_estrategico.objects.filter(descricao=descricao).count()

                    if validate==0:
                              OE=get_object_or_404(objetivo_estrategico, id=id_oes)
                              OE.descricao = descricao
                              OE.save()
                              message='Registo alterado com sucesso!'
                              status= 'success'
                    else:
                         message='A descrição inserido ja existe!!'
                         status= 'error'
                    return JsonResponse({'status':status , 'message': message })
                    

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delete_objetivo_estrategico(request):

     if request.method == "POST":
      try:
                    id_oes= request.POST.get("id")

                    OE=get_object_or_404(objetivo_estrategico, id=id_oes)
                    OE.delete()
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delete_checkbox_objetivo_estrategico(request):

     if request.method == "POST":
      try:
                    id_oes= request.POST.get("id")
                    if id_oes:
                         id_oes = id_oes.split(",") 
                         objetivo_estrategico.objects.filter(id__in=id_oes).delete()
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

def list_create_objetivo_estrategico(request):

    oes_list = objetivo_estrategico.objects.all()
    paginator = Paginator(oes_list, 7)

    page_number = request.GET.get("page")  # Obter o número da página da URL
    oes = paginator.get_page(page_number)

    return render(request, "master/GOE/index.html", {"objetivo_estrategico":oes})

#end modulo objetivo_estrategico

#start modulo Rastreabilidade
def list_rastreabilidade(request):

     query = '''
              select ras.id as id, ras.descricao as descricao, me.descricao as meta, me.id as id_meta
              from master_rastreabilidade as ras
              left join master_meta as me on ras.id_tabela_meta=me.id
             '''
     with connection.cursor() as cursor:
          cursor.execute(query)

          colunas = [col[0] for col in cursor.description] 
          resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]

          ras_list = resultados
          me_list = list(meta.objects.all())
          paginator = Paginator(ras_list, 7)
          print(paginator)
          page_number = request.GET.get("page")  
          oes = paginator.get_page(page_number)

          return render(request, "master/RAS/index.html", {"rastreabilidade":oes,"meta":me_list}) 

@csrf_exempt
def create_rastreabilidade(request):

    if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_tabela_meta = request.POST.get("id_tabela_meta")
                    status = "1"

                    validate = rastreabilidade.objects.filter(descricao=descricao).count()

                    if validate==0:
                              rastreabilidade.objects.create(
                                   descricao=descricao,
                                   status=status,
                                   id_tabela_meta=id_tabela_meta
                              )
                              message='Registo criado com sucesso!'
                              status= 'success'
                    else:
                          message='A descrição inserido ja existe!!'
                          status= 'error'

                    return JsonResponse({'status':status, 'message': message })

                   
      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def editar_rastreabilidade(request):

     if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_ras= request.POST.get("id")
                    id_tabela_meta= request.POST.get("id_tabela_meta")

                    RA=get_object_or_404(rastreabilidade, id=id_ras)
                    RA.descricao = descricao
                    RA.id_tabela_meta = id_tabela_meta
                    RA.save()
                    return JsonResponse({'status': 'success', 'message': 'Registo alterado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@csrf_exempt
def delete_rastreabilidade(request):

     if request.method == "POST":
      try:
                    id_ras= request.POST.get("id")

                    OE=get_object_or_404(rastreabilidade, id=id_ras)
                    OE.delete()
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delete_checkbox_rastreabilidade(request):

     if request.method == "POST":
      try:
                    id_ras= request.POST.get("id")
                    if id_ras:
                         id_ras = id_ras.split(",") 
                         rastreabilidade.objects.filter(id__in=id_ras).delete()
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

#End modulo Rastreabilidade
#start modulo Mapeamento 

def list_meta(request):
     query = '''
               select ME.id as id, ME.descricao as descricao, KPI.descricao as kpi, KPI.id as id_kpi
               from master_meta as ME
               left join master_kpi as KPI on ME.id_kpi=KPI.id
               '''
     with connection.cursor() as cursor:
               cursor.execute(query)

               colunas = [col[0] for col in cursor.description] 
               resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]
 
               me_list = resultados
               kpi_list= list(kpi.objects.all())
               paginator = Paginator(me_list, 7)

               page_number = request.GET.get("page")  # Obter o número da página da URL
               oes = paginator.get_page(page_number)

     return render(request, "master/ME/index.html", {"meta":oes,"kpi":kpi_list}) 


@csrf_exempt
def create_meta(request):

    if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    status = "1"
                    id_kpi=request.POST.get("id_kpi")

                    validate = meta.objects.filter(descricao=descricao).count()

                    if validate==0:
                              meta.objects.create(
                                   descricao=descricao,
                                   status=status,
                                   id_kpi=id_kpi
                              )
                              message='Registo criado com sucesso!'
                              status= 'success'
                    else:
                         message='A descrição inserido ja existe!!'
                         status= 'error'
                    return JsonResponse({'status':status, 'message': message })

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delete_meta(request):

     if request.method == "POST":
      try:
                    id_me= request.POST.get("id")

                    ME=get_object_or_404(meta, id=id_me)
                    ME.delete()
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def editar_meta(request):

     if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_me= request.POST.get("id")
                    id_kpi= request.POST.get("id_kpi")

                    ME=get_object_or_404(meta, id=id_me)
                    ME.descricao = descricao
                    ME.id_kpi = id_kpi
                    ME.save()
                    return JsonResponse({'status': 'success', 'message': 'Registo alterado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delete_checkbox_meta(request):

     if request.method == "POST":
      try:
                    id_me= request.POST.get("id")
                    if id_me:
                         id_me = id_me.split(",") 
                         meta.objects.filter(id__in=id_me).delete()
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
#end meta

#start kpi

def list_kpi(request):

     query = '''
                 select kpi.id as id,
                 kpi.descricao as descricao,
                 oe.descricao as objetivo,
                 oe.id as objetivo_estrategico
                 from master_kpi as kpi
                 left join master_objetivo_estrategico as oe on kpi.id_objeto_estrategico=oe.id

             '''
     with connection.cursor() as cursor:
          cursor.execute(query)

          colunas = [col[0] for col in cursor.description] 
          resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]

          kpi_list = resultados
          oe_list = list(objetivo_estrategico.objects.all())
          paginator = Paginator(kpi_list, 7)
          print(paginator)
          page_number = request.GET.get("page")  
          kpis = paginator.get_page(page_number)
          
          return render(request, "master/KPI/index.html", {"kpi":kpis,"meta":oe_list}) 


@csrf_exempt
def create_kpi(request):

    if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_objeto_estrategico = request.POST.get("id_objeto_estrategico")
                    status = "1"

                    validate = kpi.objects.filter(descricao=descricao).count()

                    if validate==0:
                              kpi.objects.create(
                                   descricao=descricao,
                                   status=status,
                                   id_objeto_estrategico=id_objeto_estrategico
                              )
                              message='Registo criado com sucesso!'
                              status= 'success'
                    else:
                         message='A descrição inserido ja existe!!'
                         status= 'error'

                    return JsonResponse({'status': status, 'message': message})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def editar_kpi(request):

     if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_oe = request.POST.get("id_objeto_estrategico")
                    id_kpi= request.POST.get("id")

                    
                    KPI=get_object_or_404(kpi, id=id_kpi)
                    KPI.descricao = descricao
                    KPI.id_objeto_estrategico=id_oe
                    KPI.save()

                    message='Registo alterado com sucesso!'
                    status= 'success'

                    return JsonResponse({'status': status, 'message': message})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delete_kpi(request):

     if request.method == "POST":
      try:
                    id_kpi= request.POST.get("id")

                    KPI=get_object_or_404(kpi, id=id_kpi)
                    KPI.delete()
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delete_checkbox_kpi(request):

     if request.method == "POST":
      try:
                    id_kpi= request.POST.get("id")
                    if id_kpi:
                         id_kpi = id_kpi.split(",") 
                         kpi.objects.filter(id__in=id_kpi).delete()
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
# end kpi 

@csrf_exempt
def list_OA(request):

     query = '''
                 select oa.id as id,
                 oa.descricao as descricao,
                 kpi.descricao as kpi, kpi.id as id_kpi
                 from master_objetivo_anual as oa
                 left join master_kpi as kpi on oa.id_kpi=kpi.id

             '''
     with connection.cursor() as cursor:
          cursor.execute(query)

          colunas = [col[0] for col in cursor.description] 
          resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]

          oa_list = resultados
          kpi_list = list(kpi.objects.all())
          paginator = Paginator(oa_list, 7)
          print(paginator)
          page_number = request.GET.get("page")  
          oa = paginator.get_page(page_number)
          
          return render(request, "master/OA/index.html", {"objetivo_anual":oa,"kpi":kpi_list}) 


@csrf_exempt
def create_OA(request):

    if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_kpi = request.POST.get("id_kpi")
                    status = "1"

                    validate = objetivo_anual.objects.filter(descricao=descricao).count()

                    if validate==0:
                         objetivo_anual.objects.create(
                                   descricao=descricao,
                                   status=status,
                                   id_kpi=id_kpi
                                  )
                         message='Registo criado com sucesso!'
                         status= 'success'
                    else:
                         message='A descrição inserido ja existe!!'
                         status= 'error'
                    return JsonResponse({'status':status, 'message': message })
            
      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def editar_OA(request):

    if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_oa = request.POST.get("id")
                    id_kpi = request.POST.get("id_kpi")
                    status = "1"

                    OE=get_object_or_404(objetivo_anual, id=id_oa)
                    OE.descricao = descricao
                    OE.id_kpi=id_kpi
                    OE.save()
                    return JsonResponse({'status': 'success', 'message': 'Registo alterado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delete_OA(request):

     if request.method == "POST":
      try:
                    id_OA= request.POST.get("id")

                    OA=get_object_or_404(objetivo_anual, id=id_OA)
                    OA.delete()
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delete_checkbox_OA(request):

     if request.method == "POST":
      try:
                    id_oa= request.POST.get("id")
                    if id_oa:
                         id_oa = id_oa.split(",") 
                         objetivo_anual.objects.filter(id__in=id_oa).delete()
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def list_AAN(request):

     query = '''
                 select aan.id as id,
                 aan.descricao as descricao,
                 oa.descricao as objetivo_anual,
                 aan.data_inicio as data_inicio,
                 aan.data_fim as data_fim,
                 aan.id_objetivo_anual as id_objetivo_anual
                 from master_atividade_anual as aan
                 left join master_objetivo_anual as oa on aan.id_objetivo_anual=oa.id

             '''
     with connection.cursor() as cursor:
          cursor.execute(query)

          colunas = [col[0] for col in cursor.description] 
          resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]

          aan_list = resultados
          oa_list = list(objetivo_anual.objects.all())
          paginator = Paginator(aan_list, 7)
          print(paginator)
          page_number = request.GET.get("page")  
          oa = paginator.get_page(page_number)
          
          return render(request, "master/AAN/index.html", {"atividade_anual":oa,"objetivo_anual":oa_list}) 

@csrf_exempt
def create_AAN(request):

    if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_objetivo_anual = request.POST.get("id_objetivo_anual")
                    data_inicio = request.POST.get("data_inicio")
                    data_fim = request.POST.get("data_fim")
                    status = "1"


                    validate = atividade_anual.objects.filter(descricao=descricao).count()

                    if validate==0:
                               atividade_anual.objects.create(
                                   descricao=descricao,
                                   status=status,
                                   id_objetivo_anual=id_objetivo_anual,
                                   data_inicio=data_inicio,
                                   data_fim=data_fim,
                              )
                               message='Registo criado com sucesso!'
                               status= 'success'
                    else:
                         message='A descrição inserido ja existe!!'
                         status= 'error'
                    return JsonResponse({'status':status, 'message': message })

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def editar_AAN(request):

    if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_objetivo_anual = request.POST.get("id_objetivo_anual")
                    data_inicio = request.POST.get("data_inicio")
                    data_fim = request.POST.get("data_fim")
                    id_ann = request.POST.get("id")

                    AAN=get_object_or_404(atividade_anual, id=id_ann)
                    AAN.descricao = descricao
                    AAN.id_objetivo_anual = id_objetivo_anual
                    AAN.data_inicio = data_inicio
                    AAN.data_fim = data_fim
                    AAN.save()
                    return JsonResponse({'status': 'success', 'message': 'Registo alterado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delete_AAN(request):

     if request.method == "POST":
      try:
                    id_AAN= request.POST.get("id")

                    AAN=get_object_or_404(atividade_anual, id=id_AAN)
                    AAN.delete()
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delete_checkbox_AAN(request):

     if request.method == "POST":
      try:
                    id_aan= request.POST.get("id")
                    if id_aan:
                         id_aan = id_aan.split(",") 
                         atividade_anual.objects.filter(id__in=id_aan).delete()
                         
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

#start acao

@csrf_exempt
def list_AC(request):

     query = '''
                 select ac.id as id,
                 ac.descricao as descricao,
                 aa.descricao as atividade_anual,
                 ac.obs as obs,
                 ac.id_departamento_responsavel as id_departamento_responsavel,
                 ac.responsavel_nome as responsavel_nome,
                 ac.id_departamento_auxiliar as id_departamento_auxiliar,
                 ac.responsavel_auxiliar_nome as responsavel_auxiliar_nome,
                 p.descricao as processo,
                 ac.data_inicio as data_inicio,
                 ac.data_fim as data_fim,
                 ac.id_processo as id_processo,
                 ac.id_atividade_anual as id_atividade_anual,
                 dp.descricao as departamento_responsavel,
                 dp_aux.descricao as departamento_auxiliar
                 from master_acao as ac
                 left join master_atividade_anual as aa on ac.id_atividade_anual=aa.id
                 left join master_processo as p on ac.id_processo=p.id
                 left join master_departamento as dp on ac.id_departamento_responsavel=dp.id
                 left join master_departamento as dp_aux on ac.id_departamento_auxiliar=dp_aux.id

             '''
     with connection.cursor() as cursor:
          cursor.execute(query)

          colunas = [col[0] for col in cursor.description] 
          resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]

          ac_list = resultados
          aan_list = list(atividade_anual.objects.all())
          p_list = list(processo.objects.all())
          dp_list = list(departamento.objects.all())

          paginator = Paginator(ac_list, 7)
          print(paginator)
          page_number = request.GET.get("page")  
          oa = paginator.get_page(page_number)
          
          return render(request, "master/AC/index.html", {"acao":ac_list,"atividade_anual":aan_list,"processo":p_list,"departamento":dp_list}) 

@csrf_exempt
def create_AC(request):

    if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_atividade_anual = request.POST.get("id_atividade_anual")
                    obs = request.POST.get("obs")
                    departamento = request.POST.get("departamento")
                    nome_responsavel = request.POST.get("nome_responsavel")
                    departamento_auxiliar = request.POST.get("departamento_auxiliar")
                    nome_responsavel_auxiliar = request.POST.get("nome_responsavel_auxiliar")
                    id_processo = request.POST.get("id_processo")
                    data_inicio = request.POST.get("data_inicio")
                    data_fim = request.POST.get("data_fim")
                    status = "1"

                    validate = acao.objects.filter(descricao=descricao).count()

                    if validate==0:
                              acao.objects.create(
                                        descricao=descricao,
                                        status=status,
                                        id_atividade_anual=id_atividade_anual,
                                        id_processo=id_processo,
                                        id_departamento_responsavel=departamento,
                                        responsavel_nome=nome_responsavel,
                                        id_departamento_auxiliar=departamento_auxiliar,
                                        responsavel_auxiliar_nome=nome_responsavel_auxiliar,
                                        data_inicio=data_inicio,
                                        obs=obs,
                                        data_fim=data_fim,
                                   )
                              message='Registo criado com sucesso!'
                              status= 'success'
                    else:
                         message='A descrição inserido ja existe!!'
                         status= 'error'
                    return JsonResponse({'status':status, 'message': message })

                    
      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@csrf_exempt
def editar_AC(request):

    if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_atividade_anual = request.POST.get("id_atividade_anual")
                    id_processo = request.POST.get("id_processo")
                    obs = request.POST.get("obs")
                    data_inicio = request.POST.get("data_inicio")
                    data_fim = request.POST.get("data_fim")
                    id_ac = request.POST.get("id")
                    departamento = request.POST.get("departamento")
                    nome_responsavel = request.POST.get("nome_responsavel")
                    departamento_auxiliar = request.POST.get("departamento_auxiliar")
                    nome_responsavel_auxiliar = request.POST.get("nome_responsavel_auxiliar")

                    AC=get_object_or_404(acao, id=id_ac)
                    AC.descricao = descricao
                    AC.id_atividade_anual = id_atividade_anual
                    AC.obs = obs
                    AC.id_departamento_responsavel=departamento
                    AC.responsavel_nome=nome_responsavel
                    AC.id_departamento_auxiliar=departamento_auxiliar
                    AC.responsavel_auxiliar_nome=nome_responsavel_auxiliar
                    AC.id_processo = id_processo
                    AC.data_inicio = data_inicio
                    AC.data_fim = data_fim
                    AC.save()

                    return JsonResponse({'status': 'success', 'message': 'Registo alterado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delete_AC(request):

     if request.method == "POST":
      try:
                    id_ac= request.POST.get("id")

                    OA=get_object_or_404(acao, id=id_ac)
                    OA.delete()
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delect_checkbox_AC(request):

     if request.method == "POST":
      try:
                    id_ac= request.POST.get("id")
                    if id_ac:
                         id_ac = id_ac.split(",") 
                         acao.objects.filter(id__in=id_ac).delete()
                         
                    return JsonResponse({'status': 'success', 'message': 'Registo apagado com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
