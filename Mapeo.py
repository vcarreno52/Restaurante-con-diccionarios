
class Mapeo:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.dicmenu = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    
    def obtener_diccionario(self):
        return self.dicmenu
    

class MapeoInfantil(Mapeo):
    def __init__(self, nombre, precio, cantidad, figurita):
        super().__init__(nombre, precio, cantidad)
        self.dicmenu ["figurita"] = figurita
    
 
class MapeoAdultos(Mapeo):
    def __init__(self, nombre, precio, cantidad, bebida, tamano):
        super().__init__(nombre, precio, cantidad)
        self.dicmenu ["bebida"] = bebida
        self.dicmenu ["tamano"] = tamano


class MaperoAnciano(Mapeo):
    def __init__(self, nombre, precio, cantidad, bebida):
        super()._init_(nombre, precio, cantidad)
        self.dicmenu ["bebida"] = bebida

class MaperoAnsiosos(Mapeo):
    def __init__(self, nombre, precio, cantidad, ansiolíticos):
        super()._init_(nombre, precio, cantidad)
        self.dicmenu ["ansioliticos"] = ansiolíticos

class MaperoAlcoholico(Mapeo):
    def __init__(self, nombre, precio, cantidad, alcolhol, tipo):
        super()._init_(nombre, precio, cantidad)
        self.dicmenu ["Alcolhol"] = alcolhol
        self.dicmenu ["tipo"]= tipo 


    
A= MapeoInfantil("Juan", 2000, 1, "Dinosario")
print(A.obtener_diccionario())

