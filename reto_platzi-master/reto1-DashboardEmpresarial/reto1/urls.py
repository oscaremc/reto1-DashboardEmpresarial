
from django.contrib import admin
from django.urls import path
from reto1 import views as local_views
from dashboards import views as dashboards_views
from dashboards.homeview import homeview
from dashboards.views import FormCompanyView

#hay que regresar una instancia de HttpResponse con el contenido que nosotros queramos
urlpatterns = [
    path('', homeview.home, name = 'home'),
    path('registercompany/', FormCompanyView.index, name = 'Registrar Compañía'),
    path('savecompany/', FormCompanyView.process_form, name = 'Guardar Compañía'),
    path('views/detalle.html/', FormCompanyView.detalles, name = 'detalles'),
    path('views/index.html/', FormCompanyView.views_index, name = 'detalles'),
    path('views/detalle.html/crear.html/', FormCompanyView.views_crear, name = 'crear'),
    path('views/detalle.html/editar.html', FormCompanyView.views_editar, name = 'editar'),
]