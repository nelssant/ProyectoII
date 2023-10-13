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
8. **Operaciones del Menu**
   1. Permite al usuario el poder agregar un producto.
   2. Le permite al usuario poder buscar un producto mediante el nombre o el codigo (Con caracteres que se encuentren en dichos parametros(
   3. Le permitirá al usuario  poder modificar el producto menos el código.
   4. Unicamente leerá el archivo de nuevo, si el usuario ya hizo cambios, al seleccionar esta opción se mostrarán dichos cambios.
   5. Le permitirá al usuario el poder finalizar la ejecución de la aplicación
  
