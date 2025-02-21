# Restaurante-con-diccionarios
🍽️ Restaurante Diccionario

Este proyecto implementa un sistema de gestión de menús para un restaurante mediante clases en Python y una base de datos en MySQL. Permite registrar y almacenar información sobre diferentes tipos de menú.


📌 Estructura del Proyecto

El proyecto está dividido en los siguientes módulos:

1️⃣ Rest (Rest.py)

El módulo Rest constituye el núcleo de la aplicación. En él se definen las clases que representan las entidades principales del sistema, así como la lógica de negocio que rige su comportamiento. Este módulo es el encargado de encapsular la complejidad del dominio y ofrecer una interfaz clara y coherente para el resto de los componentes.

2️⃣ Mapeo (Mapeo.py)

El módulo Mapeo actúa como un puente entre las instancias de las clases definidas en Rest y el mundo exterior. Su función principal es tomar objetos de estas clases y convertirlos en estructuras de datos más simples, como diccionarios. Esta transformación facilita la manipulación y el intercambio de información entre los diferentes módulos de la aplicación.

Ejemplo de uso:

                from Mapeo import MapeoInfantil
                A = MapeoInfantil("Juan", 2000, 1, "Dinosaurio")
                print(A.obtener_diccionario())

3️⃣ Conexión con MySQL (Conexion.py)

El módulo Conexion se encarga de la persistencia de los datos. Su labor consiste en recibir las estructuras de datos generadas por Mapeo, desempaquetarlas y adaptarlas al formato requerido por la base de datos MySQL. Este módulo establece la comunicación con la base de datos y ejecuta las operaciones necesarias para almacenar la información de manera eficiente y segura.

Ejemplo de conexión:

                import mysql.connector
                
                conexion = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="menu"
                )
                cursor = conexion.cursor()
                
                Ejemplo de inserción de datos:
                
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

📂 Esquema de la Base de Datos

Para modelar los diferentes tipos de menús (Vegetariano, Para compartir, Infantil, etc.), se ha creado una tabla independiente para cada uno de ellos. Cada tabla contiene información específica sobre los platos incluidos en ese menú en particular, como su nombre, descripción, precio y otros detalles relevantes.

Además de estas tablas específicas de menú, se ha diseñado una tabla central llamada menuitem. Esta tabla actúa como una clase padre y almacena información general sobre todos los platos, independientemente del tipo de menú al que pertenezcan. De esta manera, se evita la redundancia de datos y se facilita la gestión y actualización de la información común a todos los platos.

#Resultados

El código genera diccionarios para facilitar la gestión de información de menús y platos. Este formato simplifica el procesamiento y la transferencia de datos entre módulos. Luego, los diccionarios se cargan a MySQL, asegurando la persistencia y el acceso centralizado a la información. La estructura de tablas optimiza el almacenamiento y la consulta de datos. En resumen, el código ofrece una solución eficiente, flexible y escalable para la gestión de menús y platos.



