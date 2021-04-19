"""
Vistas del proyecto
"""
#django
from django.http import HttpResponse
import pdb
#utilities

from datetime import datetime


import json

#siempre recibe un request, el objeto del request y regresa una respuesta, pero no tenemos que escribir la respuesta a mano
#para escribir una respuesta http tenemos que importar una herramienta de Django: HttpResponse
