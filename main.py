#import Rest, Mapeo, Conexion
from Mapeo import MapeoAdultos
from Rest import menu_adultos
from Conexion import subir_adultos

A= MapeoAdultos("Juan", 2000, 1, "Gaseosa","Grande")

subir_adultos(A.obtener_diccionario())  


