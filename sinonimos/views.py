from django.http import JsonResponse
from sinonimos.scraping import retorna_sinonimos

def sinonimo(request):
    palavra = request.GET.get('q')
    sinonimos = retorna_sinonimos(palavra)
    response = {
        "results": sinonimos
    }
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})