#Clase 2: Resolucion desafios   

#Lectura y escritura de archivos
#🧗‍♀️ Desafío I: Creá un archivo de prueba (bio.txt) en la carpeta destinada a los prácticos de la materia.
"""#Escribir archivos
with open("bio.txt","a") as archivo:
    archivo.close"""

#🧗‍♀️ Desafío II: Investigá sobre los métodos os.mkdir() y os.listdir()
"""os.mkdir()
El método en Python se usa para crear un directorio llamado ruta con el modo numérico especificado. 
Este método genera FileExistsError si el directorio que se va a crear ya existe.

Sintaxis: os.mkdir(ruta, modo = 0o777, *, dir_fd = None)

Parámetro:
ruta : un objeto similar a una ruta que representa una ruta del sistema de archivos. 
Un objeto similar a una ruta es un objeto de cadena o bytes que representa una ruta.
modo(opcional): un valor entero que representa el modo del directorio que se creará. 
Si se omite este parámetro, se utiliza el valor predeterminado Oo777.
dir_fd(opcional): un descriptor de archivo que hace referencia a un directorio. 
El valor predeterminado de este parámetro es None.
Si la ruta especificada es absoluta, dir_fd se ignora."""

"""La función os.listdir() devuelve una lista que contiene los nombres de las entradas (archivos y directorios) 
del directorio indicado (path). La lista no sigue ningún tipo de orden y no se incluyen las entradas 
intaxis: os.listdir(ruta)

Parámetros:
ruta(opcional): ruta del directorio

Tipo de retorno: este método devuelve la lista de todos los archivos y directorios en la ruta especificada. 
El tipo de retorno de este método es list ."""

#🧗‍♀️ Desafío III: Abrí el archivo bio.txt y escribí una mini biografía de presentación. 
"""with open("bio.txt","a") as archivo:
    archivo.write(" Mi nombre es Juana, tengo 21 anos. \n Estudio Administracion y estoy en el ultimo ano.")"""

# Para pensar 🤔:¿Cómo darías formato al texto que estas creando?
"""Usamos esto:
Enter → \n
Tabulación→ \t
Espacio → \s
"""

#Para pensar 🤔:
#¿Qué diferencias notás? ¿Para qué sirve cada método? ¿Que tipo de dato obtenemos en cada caso? Usá la función type() para explorarlo:
"""
.read() Lee del archivo según el número de bytes de tamaño. Si no se pasa ningún, entonces lee todo el archivo.

.readline() Lee como máximo el número de caracteres de tamaño de la línea. Esto continúa hasta el final de la línea y 
luego regresa.

.readlines() Esto lee las líneas restantes del objeto de archivo y las devuelve como una lista.
"""

#🧗‍♀️Desafio IV: Descargá el archivo manipulacion_archivos.txt y creá un programa que lea su contenido y lo imprima en pantalla el resultado.
"""
archivo = (open("manipulacion_archivos.txt","r"))
print(archivo.read())

archivo.close()
"""
#Para pensar 🤔: ¿Creés que habrá una forma más práctica de leer archivos estructurados o tabulados?
"""
with open("manipulacion_archivos.txt","r") as archivo:
    texto = archivo.read()
    print(texto)

archivo.close()
"""
#Rutas absolutas y relativas

#las rutas relativas: especifica la ruta de un archivo en referencia al directorio en el que estas parado
# las rutas absolutas: especifica donde se encuentra un archivo pero haciendo referencia del directorio raiz del sistema operativo
#cuando tenes la ruta absoluta tenes que cambiar los / por "\" p "//"
#lo que pasa es que cuanod se lo mandas a alguien ese tiene que tener los mismos directorios/carpetas, por eso conviene usar rutas relativas
