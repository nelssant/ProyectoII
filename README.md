# ProyectoII-Archivos, Estructuras de control y funciones

## Gestión de un archivo con productos

## Instrucciones de Uso:

**Ejecución del programa**
   - La aplicación solicitará al usuario la ruta de la carpeta que desea.
   - La aplicación solicitará al usuario la ruta del archivo que desea.
   - Si la ruta de la carpeta es incorrecta, la aplicación en automático creará una nueva carpeta denominada ProyectoII en el apartado de descargas.
   - SI la ruta de la carpeta es correcta pero, el nombre del archivo es incorrecto; la aplicación creará un nuevo archivo denteo de la carpeta (ingresada por el usuario o creada por la app) con el nombre que el usuario ingresó al principio.
   - El programa consultará al usuario si deseea editar el archivo, si la respuesta es no; el programa leerá la informacion que tenga dicho archivo mostrándola en la terminal, luego de ello; el programa finalizará.
   - Si el usuario indica que si desea editar el archivo, mostrará el contenido del archivo y un menú.
   - Cuando el usuario seleccione la opción 1 (Agregar producto), el programa solicitará los atributos para que el usuario los ingrese; de igual forma, el programa verificará si el código que el usuario intenta ingresar ya existe y le solicitará un nuevo código de producto hasta que el usuario ingrese un código que no exista, luego continuará solicitandole el resto de atributos.
   - Cuando el usuario seleccione la opción 2 (Buscar producto), el programa le solicitará que ingrese ya sea algun valor que se encuentre en el nombre del producto o en el código y éste le mostrará al usuario todos los productos que tengan coincidencias.
        - Por ejemplo, si el usuario ingresa la letra a y ésta aparece ya sea en el nombre o en el código de los productos, mostrará todos los que tengan dicha coincidencia; si de 1000 productos hay 999 que coinciden, se mostrarán los 999 artículos.
     - Cuando el usuario seleccione la opción 3 (Modificar datos de un producto), el usuario debe de ingresar el código del producto que desea modificar, luego el programa al encontrar dicho producto en el archivo; le solicitara los nuevos datos para los atributos menos el código
     - Cuando el usuario seleccione la opción 4 (Leer de nuevo), el programa mostrará nuevamente la información de todo el archivo (Y si el archivo tuvo modificaciones, la información será con las nuevas modificaciones)
     - Cuando el usuario seleccione la opción 5 (Salir), el programa mostrara nuevamente el contenido del archivo y finaliará.

# Funciones y Estructuras definidas

1  **Menú de opciones (mostrar_menu)**
   Se agregan 5 opciones disponibles:
   1. Agregar Producto
   2. Buscar producto
   3. Modificar datos de un producto
   4. Leer de nuevo
   5. Salir
      
2. **Producto y atributos (Crear_Productto)**
   Se agregan los atributos del producto:
   1. Nombre del producto
   2. Código del producto
   3. Precio del producto
   4. Proveedor del producto
   5. Existencia del producto
   6. Estado del producto
   7. Descuento del producto
  
  3. **Lesctura del archivo (lectura)**
     Esta funcion solo servirá para poder leer y mostrar cada línea de contenido dentro del archivo.

  4. **Manipulación del archivo (manipulacion_archivo)**
     EN esta estructura vamos a editar el archivo unicamente si el usuario indica que lo quiere editar.
  
  5. **Buscar un producto (buscar_producto)**
     Buscara el producto ya sea por palabras que contenga el nombre o el código y nos imprimierá todas las coincidencias

  6. **Modificar datos (modificar_datos)**
     Permitirá buscar un producto mediante el c►digo y con base a ello, podremos editar todos los atributos menos el código

-------------------------------------------------------------------------------------------------------------------------------
# Resumen  de la lógica y funcionamiento de las funciones definidas

1. **Operaciones con el Menu**
   1. Permite al usuario el poder agregar un producto.
   2. Le permite al usuario poder buscar un producto mediante el nombre o el codigo (Con caracteres que se encuentren en dichos parametros)
   3. Le permitirá al usuario  poder modificar el producto menos el código.
   4. Unicamente leerá el archivo de nuevo, si el usuario ya hizo cambios, al seleccionar esta opción se mostrarán dichos cambios.
   5. Le permitirá al usuario el poder finalizar la ejecución de la aplicación

2. **Operaciones con el producto y sus atributos**
   - La función unicamente se utilizará para poder manipular el archivo, es decir; el programa la estará llamando para poder recorrer el archivo y realizar la actividad que corresponda según la lógica:
        - Al agregar el producto, ayudará a poder validar que el código no esté repetido

3. **Operaciones con la función buscar_producto**
   - Permite buscar un producto mediante el código, dado que el mismo no puede repetirse, siempre devolvera un solo artículo o proudcto.
   - Con base a la variable global ruta, sabemos en dónde está el archivo que debemos leer.
   - Lo abrimos, leemos y buscamos la información en cada línea del archivo y solo en la columna del código.
   - Si no se encuentra el producto, no se podrá mostrar nada.

4. **Operaciones con la función modificar_datos**
   - Al igual que la función buscar_producto, está al inicio realiza algo similar, pero nos va a solicitar cada atributo autorizado a modificación y cuando ingresemos el último atributo, guarda los cambios en el archivo y se cierra.
------------------------------------------------------------------------------------------------------------------------------------
# Explicación del programa a nivel técnico

1. Cuando el usuario ejecuta el programa, éste lo que realiza es entrar a un ciclo While y solicita al usuario que ingrese la ruta de la carpeta y el nombre del archivo.
2. Ahora que el usuario ya ha ingresado la información solicitada, ingresa a las validaciones (los if), primero valida si la carpeta existe, si ésta existe entonces ingresa a otro if y valida si el archivo exite, si el archivo existe consulta al usuario si desea editarlo.
3. El usuario ingresa su elección en la variable global (edicion1) y el programa a la varibalbe global denominada rutas, le asigna la ruta completa del archivo (archivo_path)
4. En dado caso el punto 2 antes expuesto no resulta verdadero y resulta que el usuario ingreso bien la ruta de la carpeta pero no hay ningún archivo en ella, el programa en automático lo crea y sigue el flujo (Punto 3)
5. SI el punto 2 resulta falso en ambas validaciones, la aplicación ingresa a las descargas y os crea una carpeta denominada ProyectoII y crea el archivo con el nombre que el usuario le dió al inicio.
6. Ahora se repite el paso 3.
7. Ahora que ya existe un archivo, desplegamos las funciones y condiciones: Si el usuario ha ingresado que no dese editar el archivo, en automático el programa muestra la información que contiene dicho archivo y finaliza.
8. Si el usuario selecciona que si desea editar el archivo, en automático el programa ingresa al While que se encuentra en la validacion:
   ```python
   if edicion1.lower() == "yes" or edicion2.lower() == "yes":)
   ```
   Al ingresar a la condición anterior, en automático llamremos a la función y por ende nos pedirá una opción que se almacenará en la variable menu.
   ```python
   mostrar_menu()
   ```
9. Si la opción es 1, ingresará en automático a solicitar el nombre y el código del producto.
10. Despues de que el usuario ingrese el código, el programa ingresa a un ciclo while el cual será falso hasta que el código no aparezca en el archivo; mientras el código del producto aparezca en el archivo, el ciclo while siempre estará solicitando al usuario que ingrese el código corrrecto.
11. Cuando el ciclo es falso, en automático llamamos a la función:
    ```python
    manipulacion_archivo()
    ```
   Esta función se maneja con base a a las variables edicion1 y edicion2
   - La lógica es la misma para ambas variables, sin embargo el detalle está en la ruta almacenada.
   - Con esta función creamos una variable denominada varibale la cual contendrá a la función crear_producto puesto que ésto nos servirá para poder anotar los datos que ingrese el usuario.
   ```python
     variable = crear_producto(nombre, codigo, precio, proveedor, existencia, estado, descuento)
            with open(archivo_path, 'a') as archivo:
                archivo.write("\t".join(map(str, variable.values())) + "\n")
                print("Archivo editado exitosamente.")
        except FileNotFoundError:
            print(f"El archivo '{archivo_path}' no se encontro.")
        except Exception as e:
            print(f"Se produjo un error: {e}")
   ```
12. Si la opción es 2, en automático llamamos a la función buscar_producto
13. Si la opción es 3, en automático llamamos a la función modificar_datos
14. Si la opción es 4, en automático llamamos a la función lectura
15. Si la opción es 5, en automático salimos del programa
16. De otro modo, si el usuario ingresa una opción no parametrizada, el programa saldrá
