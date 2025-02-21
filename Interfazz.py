
import tkinter as tk
from tkinter import ttk
from Conexion import *
from  Mapeo import * 
from Rest import *

def crear_y_subir_menu():
    tipo_menu = combo_tipo_menu.get()
    nombre = entrada_nombre.get()
    precio = float(entrada_precio.get())
    cantidad = int(entrada_cantidad.get())

    datos_menu = {"nombre": nombre, "precio": precio, "cantidad": cantidad}

    if tipo_menu == "Infantil":
        figurita = entrada_figurita.get()
        menu = menu_infantil(nombre, precio, cantidad, figurita)
        datos_menu["figurita"] = figurita
        subirinfantil(datos_menu)
    elif tipo_menu == "Adultos":
        bebida = entrada_bebida.get()
        tamano = entrada_tamano.get()
        menu = menu_adultos(nombre, precio, cantidad, bebida, tamano)
        datos_menu["bebida"] = bebida
        datos_menu["tamano"] = tamano
        subir_adultos(datos_menu)
    elif tipo_menu == "Ancianos":
        bebida = entrada_bebida.get()
        menu = menu_ancianos(nombre, precio, cantidad, bebida)
        datos_menu["bebida"] = bebida
        subir_ancianos(datos_menu)
    elif tipo_menu == "Ansiosos":
        ansiolitico = int(entrada_ansiolitico.get())
        menu = menu_ansiosos(nombre, precio, cantidad, ansiolitico)
        datos_menu["ansiolitico"] = ansiolitico
        subir_ansiosos(datos_menu)
    elif tipo_menu == "Alcohólico":
        alcohol = entrada_alcohol.get()
        tipo = entrada_tipo_alcohol.get()
        menu = menu_alcólicos(nombre, precio, cantidad, alcohol, tipo)
        datos_menu["alcohol"] = alcohol
        datos_menu["tipo"] = tipo
        subir_alcoholicos(datos_menu)
    elif tipo_menu == "Vegetariano":
        verduras = entrada_verduras.get()
        menu = menu_vegetariano(nombre, precio, cantidad, verduras)
        datos_menu["verduras"] = verduras
        subir_vegetariano(datos_menu)
    elif tipo_menu == "Para compartir":
        platillo = entrada_platillo.get()
        menu = menu_para_compartir(nombre, precio, cantidad, platillo)
        datos_menu["platillo"] = platillo
        subir_para_compartir(datos_menu)

    print(f"Menú {tipo_menu} creado y subido a la base de datos.")

ventana = tk.Tk()
ventana.title("Crear y Subir Menú")
ventana.geometry("400x300")  # Tamaño inicial


# Etiquetas y entradas comunes
etiqueta_nombre = ttk.Label(ventana, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0)
entrada_nombre = ttk.Entry(ventana)
entrada_nombre.grid(row=0, column=1)

etiqueta_precio = ttk.Label(ventana, text="Precio:")
etiqueta_precio.grid(row=1, column=0)
entrada_precio = ttk.Entry(ventana)
entrada_precio.grid(row=1, column=1)

etiqueta_cantidad = ttk.Label(ventana, text="Cantidad:")
etiqueta_cantidad.grid(row=2, column=0)
entrada_cantidad = ttk.Entry(ventana)
entrada_cantidad.grid(row=2, column=1)

# Selección de tipo de menú
etiqueta_tipo_menu = ttk.Label(ventana, text="Tipo de menú:")
etiqueta_tipo_menu.grid(row=3, column=0)
opciones_menu = ["Infantil", "Adultos", "Ancianos", "Ansiosos", "Alcohólico", "Vegetariano", "Para compartir"]
combo_tipo_menu = ttk.Combobox(ventana, values=opciones_menu)
combo_tipo_menu.current(0)  # Establecer el primer elemento como predeterminado
combo_tipo_menu.grid(row=3, column=1)

# Etiquetas y entradas específicas (se mostrarán según el tipo de menú)
etiqueta_figurita = ttk.Label(ventana, text="Figurita:")
entrada_figurita = ttk.Entry(ventana)
etiqueta_bebida = ttk.Label(ventana, text="Bebida:")
entrada_bebida = ttk.Entry(ventana)
etiqueta_tamano = ttk.Label(ventana, text="Tamaño:")
entrada_tamano = ttk.Entry(ventana)
etiqueta_ansiolitico = ttk.Label(ventana, text="Ansiolítico:")
entrada_ansiolitico = ttk.Entry(ventana)
etiqueta_alcohol = ttk.Label(ventana, text="Alcohol:")
entrada_alcohol = ttk.Entry(ventana)
etiqueta_tipo_alcohol = ttk.Label(ventana, text="Tipo de alcohol:")
entrada_tipo_alcohol = ttk.Entry(ventana)
etiqueta_verduras = ttk.Label(ventana, text="Verduras:")
entrada_verduras = ttk.Entry(ventana)
etiqueta_platillo = ttk.Label(ventana, text="Platillo:")
entrada_platillo = ttk.Entry(ventana)

# Función para mostrar/ocultar campos específicos
def mostrar_campos_especificos(event):
    tipo_menu = combo_tipo_menu.get()

    # Ocultar todos los campos específicos
    etiqueta_figurita.grid_forget()
    entrada_figurita.grid_forget()
    etiqueta_bebida.grid_forget()
    entrada_bebida.grid_forget()
    etiqueta_tamano.grid_forget()
    entrada_tamano.grid_forget()
    etiqueta_ansiolitico.grid_forget()
    entrada_ansiolitico.grid_forget()
    etiqueta_alcohol.grid_forget()
    entrada_alcohol.grid_forget()
    etiqueta_tipo_alcohol.grid_forget()
    entrada_tipo_alcohol.grid_forget()
    etiqueta_verduras.grid_forget()
    entrada_verduras.grid_forget()
    etiqueta_platillo.grid_forget()
    entrada_platillo.grid_forget()

    # Mostrar campos específicos según el tipo de menú seleccionado
    if tipo_menu == "Infantil":
        etiqueta_figurita.grid(row=4, column=0)
        entrada_figurita.grid(row=4, column=1)
    elif tipo_menu == "Adultos" or tipo_menu == "Ancianos":
        etiqueta_bebida.grid(row=4, column=0)
        entrada_bebida.grid(row=4, column=1)
        if tipo_menu == "Adultos":
            etiqueta_tamano.grid(row=5, column=0)
            entrada_tamano.grid(row=5, column=1)
    elif tipo_menu == "Ansiosos":
        etiqueta_ansiolitico.grid(row=4, column=0)
        entrada_ansiolitico.grid(row=4, column=1)
    elif tipo_menu == "Alcohólico":
        etiqueta_alcohol.grid(row=4, column=0)
        entrada_alcohol.grid(row=4, column=1)
        etiqueta_tipo_alcohol.grid(row=5, column=0)
        entrada_tipo_alcohol.grid(row=5, column=1)
    elif tipo_menu == "Vegetariano":
        etiqueta_verduras.grid(row=4, column=0)
        entrada_verduras.grid(row=4, column=1)
    elif tipo_menu == "Para compartir":
        etiqueta_platillo.grid(row=4, column=0)
        entrada_platillo.grid(row=4, column=1)

# Asociar función al evento de selección de tipo de menú
combo_tipo_menu.bind("<<ComboboxSelected>>", mostrar_campos_especificos)

# Botón para crear y subir menú
boton_crear_subir = ttk.Button(ventana, text="Crear y Subir ")
ventana.mainloop()
