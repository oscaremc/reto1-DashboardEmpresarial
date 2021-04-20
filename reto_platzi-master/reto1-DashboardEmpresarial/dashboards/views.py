#django
from django.shortcuts import render

#mias
from dashboards.forms import CompanyForm

# Create your views here.
"""Views"""

from django.http import HttpRequest


class FormCompanyView(HttpRequest):

    def index(request):
        company = CompanyForm()
        return render(
            request,
            "CompanyIndex.html",
            {"form":company})

    def process_form(request):
        company = CompanyForm(request.POST)
        if company.is_valid():
            company.save()
            company = CompanyForm()

        return render(
            request,
            "CompanyIndex.html",
            {"form":company},
            {"mensaje":'OK'})
        
    def detalles(request):
        detalle = CompanyForm()
        return render (request, "detalle.html", {"form":detalle})

    def views_index(request):
        views_index = CompanyForm()
        return render (request, "index.html", {"form":views_index})

    def views_crear(request):
        views_crear = CompanyForm()
        return render (request, "crear.html", {"form":views_crear})
        
    def views_editar(request):
        views_editar = CompanyForm()
        return render (request, "editar.html", {"form":views_editar})