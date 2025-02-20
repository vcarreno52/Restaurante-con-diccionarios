class MenuItem:
    def _init_(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self._precio = precio
        self.cantidad = cantidad

    def get_precio(self):
        return self._precio

    def total_price(self):
        return self.get_precio() * self.cantidad


class menu_infantil(MenuItem):
    def _init_(self, nombre: str, precio: float, cantidad: int, figurita: str):
        super()._init_(nombre, precio, cantidad)
        self.figurita = figurita

    def total_price(self):
        if self.figurita == "dinosaurio":
            return super().total_price() + 2000
        else:
            return f"ya no hay, {self.figurita}"


class menu_adultos(MenuItem):
    def _init_(self, nombre: str, precio: float, cantidad: int, bebida: str, tamano: str):
        super()._init_(nombre, precio, cantidad)
        self.bebida = bebida
        self.tamano = tamano

    def total_price(self):
        if self.tamano == "Grande":
            return super().total_price() * 1.5
        else:
            return super().total_price()


class menu_ancianos(MenuItem):
    def _init_(self, nombre: str, precio: float, cantidad: int, bebida: str):
        super()._init_(nombre, precio, cantidad)
        self.bebida = bebida


class menu_ansiosos(MenuItem):
    def _init_(self, nombre: str, precio: float, cantidad: int, ansiolítico: int):
        super()._init_(nombre, precio, cantidad)
        self.ansiolítico = ansiolítico

    def total_price(self):
        if self.ansiolítico < 1:
            return super().total_price()
        elif self.ansiolítico == 1:
            return super().total_price() * 1.5
        else:
            return 'Son demasiados ansiolíticos, relájate un poco xd'


class menu_alcólicos(MenuItem):
    def _init_(self, nombre: str, precio: float, cantidad: int, alcohol: str, tipo: str):
        super()._init_(nombre, precio, cantidad)
        self.alcohol = alcohol
        self.tipo = tipo

    def total_price(self):
        if self.tipo == "cóctel":
            return super().total_price() + 5000
        elif self.cantidad > 1:
            return super().total_price() + 2000
        else:
            return super().total_price()


class menu_vegetariano(MenuItem):
    def _init_(self, nombre: str, precio: float, cantidad: int, verduras: str):
        super()._init_(nombre, precio, cantidad)
        self.verduras = verduras


class menu_para_compartir(MenuItem):
    def _init_(self, nombre: str, precio: float, cantidad: int, platillo: str):
        super()._init_(nombre, precio, cantidad)
        self.platillo = platillo

    def total_price(self):
        if self.cantidad > 1:
            return super().total_price() * 0.9
        else:
            return super().total_price()


def precio_total(*menus):
    total = 0
    for menu in menus:
        total += menu.total_price()
    return total

