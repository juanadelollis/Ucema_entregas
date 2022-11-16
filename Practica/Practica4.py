#PRACTICA MANIPULACION DE ARCHIVOS

#Ejercicio 1:
#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada 
# letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
"""
with open("manipulacion_archivos.txt","r") as archivo:
    linea = archivo.readlines()
    if linea != "p":
       print(len(linea))
    else: 
        archivo.close
"""

#Ejercicio 2:
#Escribí un programa que lea un archivo e imprima las primeras n líneas.
"""
def leer_primeras_lineas(texto,n):
    with open(texto) as archivo:
        lineas = archivo.readlines()
    return lineas[:n]

print(leer_primeras_lineas("manipulacion_archivos.txt",2))
"""
#las utlimas dos 
"""       
def leer_primeras_lineas(texto,n):
    with open(texto) as archivo:
        lineas = archivo.readlines()
    return lineas[-n:]

print(leer_primeras_lineas("manipulacion_archivos.txt",2))
"""

#Ejercicio 3
#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.
 
"""
lista = []
with open("manipulacion_archivos.txt", "r") as archivo:
    lineas = [linea.strip('\n') for linea in archivo.readlines()]
    lista.append(lineas)

print(lista)
"""
"""
lista = []
def guardar(texto, n):
    with open(texto, "r") as archivo:
        lineas = [linea.strip('\n') for linea in archivo.readlines()]
        lista.append(lineas)
    return lineas [-n:]
    

print(guardar("manipulacion_archivos.txt",5))
"""

#Ejercicio 4
#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
"""
with open("manipulacion_archivos.txt") as archivo:
    texto = archivo.read()
    palabras = texto.split()
    num_palabras = len(palabras)
print("El archivo contiene", str(num_palabras), "palabras")
"""

#Ejercicio 5
#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y 
#lo guarde en otro archivo.
"""
patron = input("Escriba el caracter que quiere cambiar: ")
nuevo_patron = patron + "\n"

with open("Archivo2", "w") as output:
    with open("manipulacion_archivos.txt", "r") as input:
        texto = input.read()
        for line in texto:
            output.write(line.replace(patron, nuevo_patron))
"""
""" VERRRRR
import re

patron = "(f)"
with open("manipulacion_archivos.txt", "r") as original:
    with open("Archivo2", "w") as reemplazo:
        for linea in original:
                if re.search(patron, linea):
                    linea = linea.replace( patron, patron + "\n")
                reemplazo.write(linea)
"""  
"""  VERRRR
import re, glob

def reemplazar(archivo): #es el archivo de salida que tenemos que crear porque ya tenemos los de entrada
    lista_textos = glob.glob("*.txt")
    with open(archivo, "a") as arch:
        for archivo in lista_textos: 
            with open(archivo, "r") as archivo:
                texto = archivo.read()
                patron = "[f]*"
                lista = re.findall(patron, texto)
                for patron in lista:
                    arch.write(patron + "\n")
reemplazar("Archivo2")
"""
"""
# the input file
archivo1 = open("manipulacion_archivos.txt", "r")
# the output file which stores result
archivo2 = open("Archivo2", "w")
# iteration for each line in the input file
caracter = input("Escriba el caracter que quiere cambiar: ")
nuevo_caracter = caracter + "\n"

for line in archivo1:
	# replacing the string and write to output file
	archivo2.write(line.replace(caracter, nuevo_caracter))

#closing the input and output files
archivo1.close()
archivo2.close()
"""
#Ejercicio 6
#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.
""" 

def eliminar_espacios(archivo):
    with open("Archivo2", "w") as output:
        with open(archivo, "r") as input:
            texto = input.readlines()
            patron = "\n"
            for line in texto:
                output.write(line.strip(patron))
eliminar_espacios("manipulacion_archivos.txt")
"""

#Ejercicio 7
#Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir 
# y decir cuantos caracteres tiene.
"""
def linea_mas_larga(nombre):
	with open(nombre) as archivo:
		lineas = [linea.strip('\n') for linea in archivo.readlines()]
	lmaslarga = lineas[0]
	for linea in lineas:
		if len(linea) > len(lmaslarga):
			lmaslarga = linea
	return lmaslarga
 
print ("La linea con mayor longitud es: ")
print (linea_mas_larga("manipulacion_archivos.txt"))
"""

#Ejercicio 8
#Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.
"""
def combinar_archivos(archivo1, archivo2, nuevo_archivo):
    try:
        with open(archivo1,"r") as a1, open(archivo2, "r") as a2, open(nuevo_archivo, "w") as a3:
            for lineas in a1:
                a3.write(lineas)
            a3.write("\n")
            a3.write("\n")
            for lineas in a2:
                a3.write(lineas)
    except FileNotFoundError:
        print("Uno o ambos archivos no existen")

combinar_archivos("manipulacion_archivos.txt", "bio.txt","Archivo2")
"""

#Ejercicio 9
#Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
#Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con 
#respecto a la cantidad total de palabras.
# VERRRRR
"""
import re

frecuencia = {}
with open("manipulacion_archivos.txt") as archivo:
    texto = archivo.read().lower()
    patrones = re.findall("^[a-z]+", texto)
    for word in patrones:
        count = frecuencia.get(word,0)
        frecuencia[word] = count + 1
        lista = frecuencia.keys()
        for words in lista:
            print (frecuencia[words])
"""

#Ejercicio 10
#Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo 
#dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.
"""
import os,glob
def unir_txt(carpeta1, nombre):
# carpeta1 es la ruta de la carpeta
    os.chdir(carpeta1)
    lista_textos = glob.glob("*.txt")
    os.mkdir("Resultado") #me crea la carpeta
    with open ("Resultado/" + nombre, "a") as salida: 
        for archivo in lista_textos:
            with open(archivo, "r") as texto:
                salida.write(texto.read() + "/n")
unir_txt("simulacro_fi_1p_2c-juanadelollis","salida.txt")
"""
#cree la capreta resultado  con os.mkdir, y desp abris esa carpeta y creas el archivo en esa carpeta
#por eso pones with open ("Resultado/ + nombre"), si no le pongo la carpeta resultado, lo busca en carpeta1

#(../) --> mu muevo una vez para atras en la carpeta
#-------------------------------
1 #import os

2 # os . getcwd () ---> Nos indica el directorio actual
3 #print ( os . getcwd () )
4 # >>> / home / rodrigo / Desktop / 

#Con os.chdir(path) ---> nos movemos a otra carpeta.

#Path absoluto: Ruta desde carpeta root hasta el archivo o carpeta --> /home/rodrigo/Desktop/Curso/notas.txt

# Path relativo: Ruta desde carpeta actual hasta el archivo o carpeta:
# - ./ → Se refiere a la carpeta actual --> ./Documents
# - ../ → Se refiere a la carpeta padre --> ../notas.txt

"""
os.path.exists(p): Retorna True si p existe.
os.path.isfile(p): Retorna True si p es un archivo.
os.path.isdir(p): Retorna True si p es una carpeta.
os.listdir(c): Retorna una lista con los elementos de c.
os.makedir(c): Crea la carpeta c.
os.remove(p): Borra el archivo p.
os.rmdir(c): Borra la carpeta c (que debe estar vacia)
"""
#Rutas absolutas y relativas

#las rutas relativas: especifica la ruta de un archivo en referencia al directorio en el que estas parado
# las rutas absolutas: especifica donde se encuentra un archivo pero haciendo referencia del directorio raiz del sistema operativo
#cuando tenes la ruta absoluta tenes que cambiar los / por "\" p "//"
#lo que pasa es que cuanod se lo mandas a alguien ese tiene que tener los mismos directorios/carpetas, por eso conviene usar rutas relativas

