from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def artigo(request):
    return render(request, 'artigo.html')

def lista_artigos(request):
    return render(request, 'lista_artigos.html')

def sobre(request):
    return render(request, 'sobre.html')
