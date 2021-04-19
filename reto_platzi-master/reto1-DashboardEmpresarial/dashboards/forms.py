#Django
from django import forms

#propias
from dashboards.models import Company
#from dashboards.models import Market_cap

class CompanyForm(forms.ModelForm):
    #dentro de esta clase creamos otra clase para la generación de formularios: la clase Meta
    class Meta:
        #declaramos todos los datos asociados al form a crear
        model = Company
        #le decimos los campos del modelo a generar
        #pueden ser declarados uno por uno pero usamos all
        fields = '__all__'