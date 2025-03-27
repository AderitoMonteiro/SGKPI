from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import objetivo_estrategico
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator




def master_view(request):
     return render(request, "master/index.html")

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

    return render(request, "master/index.html", {"objetivo_estrategico":oes})  

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