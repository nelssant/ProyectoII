'''Este programa manipula carpetas y archivos con la finalidad de poder gestionar productos, buscandolos; editandolos o modificandolos
Autor: Nelson Santos
'''
import os

# Variables para almacenar las respuestas del usuario y la ruta del archivo
edicion1 = ""
edicion2 = ""
rutas= ""

def mostrar_menu():
    # Funcion para mostrar el menu de opciones
    print("1. Agregar Producto ")
    print("2. Buscar producto ")
    print("3. Modificar datos de un producto ")
    print("4. Leer de nuevo ")
    print("5. Salir")
    print()

def crear_producto(nombre, codigo, precio, proveedor, existencia, estado, descuento):
    # Funcion para crear un diccionario que representa un producto
    return {
        "nombre": nombre,
        "codigo": codigo,
        "precio": precio,
        "proveedor": proveedor,
        "existencia": existencia,
        "estado": estado,
        "descuento": descuento
    }

# Verifica unicamente si la carpeta y el archivo que el usuario ingresa existe; de lo contrario crea una nueva carpeta y el archivo con el nombre que le dio el usuario
while True:
    ruta = input("Por favor ingrese la ruta de la carpeta: ").strip()
    archivo_name = input("Por favor ingrese el nombre del archivo a editar con su extension: ").strip()
    if ruta and archivo_name:
        # Verificar si la ruta de la carpeta existe
        if os.path.exists(ruta):
            # Construir la ruta completa del archivo
            archivo_path = os.path.join(ruta, archivo_name)
            # Verificar si el archivo existe
            if os.path.isfile(archivo_path):
                edicion1 = input("Desea editar el archivo? yes/no ")
            else:
                with open(archivo_path, 'w'):
                    pass
                edicion1 = input("Desea editar el archivo? yes/no ")
            rutas = archivo_path
        else:
            nueva_carpeta = os.path.join(os.path.expanduser("~"), "Downloads", "ProyectoII")
            # Crear la carpeta si no existe
            if not os.path.exists(nueva_carpeta):
                os.makedirs(nueva_carpeta)
                with open(os.path.join(nueva_carpeta, archivo_name), 'w'):
                    pass
            if os.path.isfile(os.path.join(nueva_carpeta, archivo_name)):
                edicion2 = input("Desea editar el archivo? yes/no ")
            else:
                with open(os.path.join(nueva_carpeta, archivo_name), 'w'):
                    pass
                edicion2 = input("Desea editar el archivo? yes/no ")
            rutas = os.path.join(nueva_carpeta, archivo_name)
        break
    else:
        print(" ")

# Funcion para mostrar el contenido del archivo
def lectura():
    print("Mostrando contenido del archivo ")
    try:
        with open(archivo_path, 'r') as archivo:
            for linea in archivo:
                print(linea, end='')
    except FileNotFoundError:
        print("El archivo no se encontro ")
    except Exception as e:
        print("")
    try:    
        with open(os.path.join(nueva_carpeta, archivo_name), 'r') as archivo:
            for linea in archivo:
                print(linea, end='')
    except FileNotFoundError:
        print("El archivo no se encontro ")
    except Exception as e:
        print("")
lectura()

# Funcion para manipular el archivo (agregar datos)
def manipulacion_archivo():
    if edicion1.lower() == "yes":
        print("Editando el archivo ")
        try:
            variable = crear_producto(nombre, codigo, precio, proveedor, existencia, estado, descuento)
            with open(archivo_path, 'a') as archivo:
                archivo.write("\t".join(map(str, variable.values())) + "\n")
                print("Archivo editado exitosamente.")
        except FileNotFoundError:
            print(f"El archivo '{archivo_path}' no se encontro.")
        except Exception as e:
            print(f"Se produjo un error: {e}")
    if edicion2.lower() == "yes":
        print("Editando el archivo ")
        try:
            variable = crear_producto(nombre, codigo, precio, proveedor, existencia, estado, descuento)
            with open(os.path.join(nueva_carpeta, archivo_name), 'a') as archivo:
                archivo.write("\t".join(map(str, variable.values())) + "\n")
                print("Archivo editado exitosamente.")
        except FileNotFoundError:
            print(f"El archivo '{os.path.join(nueva_carpeta, archivo_name)}' no se encontro.")
        except Exception as e:
            print(f"Se produjo un error: {e}")

# Funcion para buscar un producto en el archivo
def buscar_producto():
    try:
        with open(rutas, 'r') as archivo:
            cadena_buscar = input("Ingrese parte del codigo o nombre del producto a buscar: ").strip().lower()
            encontrado = False
            for linea in archivo:
                producto = linea.strip().split("\t")
                if cadena_buscar in producto[0].lower() or cadena_buscar in producto[1].lower():
                    print("\t".join(producto))
                    encontrado = True
            if not encontrado:
                print(f"No se encontro ningun producto que contenga '{cadena_buscar}'.")
    except FileNotFoundError:
        print(f"El archivo '{rutas}' no se encontro.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

# Funcion para modificar datos de un producto en el archivo
def modificar_datos():
    try:
        with open(rutas, 'r') as archivo:
            lineas = archivo.readlines()
        codigo_modificar = input("Ingrese el codigo del producto que desea modificar: ").strip()
        encontrado = False
        for i, linea in enumerate(lineas):
            producto = linea.strip().split("\t")
            if codigo_modificar.lower() == producto[1].lower():
                # No se permite modificar el codigo, pero se pueden modificar otros atributos
                print("Producto encontrado. Ingrese los nuevos datos:")
                nombre = input("Nuevo nombre: ")
                precio = float(input("Nuevo precio: "))
                proveedor = input("Nuevo proveedor: ")
                existencia = int(input("Nueva cantidad en existencia: "))
                estado = input("Nuevo estado (A= Aprobado y R= Reprobado): ")
                descuento = float(input("Nuevo descuento: "))

                # Actualizar la linea con los nuevos datos
                lineas[i] = "\t".join([nombre, producto[1], str(precio), proveedor, str(existencia), estado, str(descuento)]) + "\n"
                encontrado = True
                print("Datos modificados exitosamente.")

        if not encontrado:
            print(f"No se encontro ningun producto con el codigo '{codigo_modificar}'.")

        # Escribir de vuelta al archivo
        with open(rutas, 'w') as archivo:
            archivo.writelines(lineas)
    except FileNotFoundError:
        print(f"El archivo '{rutas}' no se encontro.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

# Verificar si se desea editar el archivo antes de mostrar el menu
if edicion1.lower() == "yes" or edicion2.lower() == "yes":
    while True:
        print()
        mostrar_menu()
        menu = int(input("Ingrese opcion: "))
        if menu == 1:
            print("Agregando ")        
            nombre = input("Ingrese nombre del producto: ")
            codigo = input("Ingrese codigo del producto: ").strip().lower()
            while True:
                try:
                    with open(rutas, 'r') as archivo:
                        encontrado = False
                        for linea in archivo:
                            producto = linea.strip().split("\t")
                            if codigo == producto[1].lower():
                                    codigo = input("Codigo repetido; Ingrese codigo del producto: ").strip().lower()
                                    encontrado = True
                        if not encontrado:
                            precio = float(input("Ingrese el precio del producto: "))
                            proveedor = input("Ingrese el proveedor: ")
                            existencia = int(input("Ingrese la cantidad en existencia: "))
                            estado = input("Ingrese el estado A= Aprobado y R= Reprobado: ")
                            descuento = float(input("Ingrese el descuento: "))
                            manipulacion_archivo()
                            break
                except FileNotFoundError:
                    print(f"El archivo '{rutas}' no se encontro.")
                except Exception as e:
                    print(f"Se produjo un error: {e}")
        elif menu == 2:
            print("Buscando... ")
            buscar_producto()
        elif menu == 3:
            print("Modificando... ")
            modificar_datos()
        elif menu == 4:
            print("Leyendo... ")
            lectura()
        elif menu == 5:
            print("Saliendo... ")
            break
        else:
            print("Opcion no valida ")
            print()