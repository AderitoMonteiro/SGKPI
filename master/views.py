from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import objetivo_estrategico
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse




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