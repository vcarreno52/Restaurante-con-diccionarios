#import Rest, Mapeo, Conexion
from Mapeo import *
from Rest import *
from Conexion import *

A= MapeoAdultos("Juan", 2000, 1, "Gaseosa","Grande")

subir_adultos(A.obtener_diccionario())  


