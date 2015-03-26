

from highcharts.views import HighChartsBarView
from django.shortcuts import render
import random

# Create your views here.



class BarView(HighChartsBarView):

    categories = ['Empresa', 'Tecnologia', 'Desarrollo']

    @property
    def series(self):
        result = []
        for name in ('Soporte', 'Evolucion', 'Entorno', 'Mejoramiento'):
            data = []
            for x in range(len(self.categories)):
                data.append(random.randint(0, 10))
            result.append({'name': name, "data": data})
        return result