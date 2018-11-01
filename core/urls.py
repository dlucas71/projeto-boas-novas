from django.urls import path
from . import views

# app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.sobre, name='sobre'),
    path('', views.lista_artigos, name='lista_artigos'),
    path('', views.contato, name='contato'),
    path('', views.artigo, name='artigo'),
]
