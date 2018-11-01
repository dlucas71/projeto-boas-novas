from django.contrib import admin
from django.urls import include, path

from core import views
# from core import urls

urlpatterns = [
    # path('core/', include('core.urls', namespace='core')),
    path('', views.index, name='index'),
    path('core/contato/', views.contato, name='contato'),
    path('core/artigo/', views.artigo, name='artigo'),
    path('core/lista_artigos/', views.lista_artigos, name='lista_artigos'),
    path('core/sobre/', views.sobre, name='sobre'),
    path('admin/', admin.site.urls),
]
