from django.shortcuts import HttpResponse
from django.contrib import admin

# Página index
def index(request):
    return HttpResponse("It's Work!")

# Verifica que el servicio este corriendo
def health(request):
    return HttpResponse("Ok")