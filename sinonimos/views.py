from django.http import JsonResponse
from sinonimos.scraping import retorna_sinonimos
from django.shortcuts import render

def sinonimo_api(request):
    palavra = request.GET.get('q')
    sinonimos = retorna_sinonimos(palavra)
    response = {
        "results": sinonimos
    }
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})

def index(request):
    return render(request, 'index.html')