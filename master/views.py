from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import objetivo_estrategico,rastreabilidade,meta
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator


#start modulo objetivo_estrategico

def master_view(request):
     return render(request, "master/GOE/index.html")

@csrf_exempt
def create_objetivo_estrategico(request):

    if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    status = "1"

                    objetivo_estrategico.objects.create(
                         descricao=descricao,
                         status=status
                    )
                    return JsonResponse({'status': 'success', 'message': 'Registo feito com sucesso!'})

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

                    OE=get_object_or_404(objetivo_estrategico, id=id_oes)
                    OE.descricao = descricao
                    OE.save()
                    return JsonResponse({'status': 'success', 'message': 'Registo alterado com sucesso!'})

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

    ras_list = rastreabilidade.objects.all()
    me_list = list(meta.objects.all())
    paginator = Paginator(ras_list, 7)

    page_number = request.GET.get("page")  # Obter o número da página da URL
    oes = paginator.get_page(page_number)

    return render(request, "master/RAS/index.html", {"rastreabilidade":oes,"meta":me_list}) 

@csrf_exempt
def create_rastreabilidade(request):

    if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_tabela_meta = request.POST.get("id_tabela_meta")
                    status = "1"

                    rastreabilidade.objects.create(
                         descricao=descricao,
                         status=status,
                         id_tabela_meta=id_tabela_meta
                    )
                    return JsonResponse({'status': 'success', 'message': 'Registo feito com sucesso!'})

      except Exception as e:
             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def editar_rastreabilidade(request):

     if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    id_ras= request.POST.get("id")

                    RA=get_object_or_404(rastreabilidade, id=id_ras)
                    RA.descricao = descricao
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

    me_list = meta.objects.all()
    paginator = Paginator(me_list, 7)

    page_number = request.GET.get("page")  # Obter o número da página da URL
    oes = paginator.get_page(page_number)

    return render(request, "master/ME/index.html", {"meta":oes}) 


@csrf_exempt
def create_meta(request):

    if request.method == "POST":
      try:
                    descricao = request.POST.get("descricao")
                    status = "1"

                    meta.objects.create(
                         descricao=descricao,
                         status=status
                    )
                    return JsonResponse({'status': 'success', 'message': 'Registo feito com sucesso!'})

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

                    ME=get_object_or_404(meta, id=id_me)
                    ME.descricao = descricao
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