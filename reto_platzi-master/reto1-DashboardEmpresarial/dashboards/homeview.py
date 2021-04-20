from django.template.loader import get_template
from django.http import HttpResponse

class homeview():

    def home(self):
        template = get_template('CompanyIndex.html')
        return HttpResponse(template.render())

    def form(self):
        template = get_template('form.html')
        return HttpResponse(template.render())