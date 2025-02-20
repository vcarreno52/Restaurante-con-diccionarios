import mysql.connector
import Mapeo

conexion =  mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="menu"
)
cursor = conexion.cursor()

def subirinfantil(data):
    nombre = data["nombre"]
    precio = data["precio"]
    cantidad = data["cantidad"]
    figurita = data["figurita"]


    cursor.execute("INSERT INTO MenuItem (nombre, precio, cantidad) VALUES (%s, %s, %s)", 
                    (nombre, precio, cantidad))
    menu_id = cursor.lastrowid  

    cursor.execute("INSERT INTO menu_infantil (menu_id, figurita) VALUES (%s, %s)", 
                (menu_id, figurita))
    conexion.commit()

def subir_adultos(data):
    nombre, precio, cantidad, bebida, tamano = data["nombre"], data["precio"], data["cantidad"], data["bebida"], data["tamano"]

    cursor.execute("INSERT INTO MenuItem (nombre, precio, cantidad) VALUES (%s, %s, %s)", 
                   (nombre, precio, cantidad))
    menu_id = cursor.lastrowid  

    cursor.execute("INSERT INTO menu_adultos (menu_id, bebida, tamano) VALUES (%s, %s, %s)", 
                   (menu_id, bebida, tamano))
    conexion.commit()


def subir_ancianos(data):
    nombre, precio, cantidad, bebida = data["nombre"], data["precio"], data["cantidad"], data["bebida"]

    cursor.execute("INSERT INTO MenuItem (nombre, precio, cantidad) VALUES (%s, %s, %s)", 
                   (nombre, precio, cantidad))
    menu_id = cursor.lastrowid  

    cursor.execute("INSERT INTO menu_ancianos (menu_id, bebida) VALUES (%s, %s)", 
                   (menu_id, bebida))
    conexion.commit()


def subir_ansiosos(data):
    nombre, precio, cantidad, ansiolítico = data["nombre"], data["precio"], data["cantidad"], data["ansiolítico"]

    cursor.execute("INSERT INTO MenuItem (nombre, precio, cantidad) VALUES (%s, %s, %s)", 
                   (nombre, precio, cantidad))
    menu_id = cursor.lastrowid  

    cursor.execute("INSERT INTO menu_ansiosos (menu_id, ansiolítico) VALUES (%s, %s)", 
                   (menu_id, ansiolítico))
    conexion.commit()


def subir_alcoholicos(data):
    nombre, precio, cantidad, alcohol, tipo = data["nombre"], data["precio"], data["cantidad"], data["alcohol"], data["tipo"]

    cursor.execute("INSERT INTO MenuItem (nombre, precio, cantidad) VALUES (%s, %s, %s)", 
                   (nombre, precio, cantidad))
    menu_id = cursor.lastrowid  

    cursor.execute("INSERT INTO menu_alcoholicos (menu_id, alcohol, tipo) VALUES (%s, %s, %s)", 
                   (menu_id, alcohol, tipo))
    conexion.commit()


def subir_vegetariano(data):
    nombre, precio, cantidad, verduras = data["nombre"], data["precio"], data["cantidad"], data["verduras"]

    cursor.execute("INSERT INTO MenuItem (nombre, precio, cantidad) VALUES (%s, %s, %s)", 
                   (nombre, precio, cantidad))
    menu_id = cursor.lastrowid  

    cursor.execute("INSERT INTO menu_vegetariano (menu_id, verduras) VALUES (%s, %s)", 
                   (menu_id, verduras))
    conexion.commit()


def subir_para_compartir(data):
    nombre, precio, cantidad, platillo = data["nombre"], data["precio"], data["cantidad"], data["platillo"]

    cursor.execute("INSERT INTO MenuItem (nombre, precio, cantidad) VALUES (%s, %s, %s)", 
                   (nombre, precio, cantidad))
    menu_id = cursor.lastrowid  

    cursor.execute("INSERT INTO menu_para_compartir (menu_id, platillo) VALUES (%s, %s)", 
                   (menu_id, platillo))
    conexion.commit()
