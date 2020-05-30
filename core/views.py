from django.shortcuts import HttpResponse

# Página index
def index(request):
    return HttpResponse("It's Work!")

# Verifica que el servicio este corriendo
def health(request):
    return HttpResponse("Ok")