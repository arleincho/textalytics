
from import_export import resources
from lecciones.models import Leccion
from lecciones.models import Diccionario



class DiccionarioResource(resources.ModelResource):
    class Meta:
        model = Diccionario
        fields = ('id', 'name', 'language', 'description')


class LeccionResource(resources.ModelResource):
    class Meta:
        model = Leccion
        fields = ('id', 'txt', 'language', 'itf', 'source', 'timeref')
