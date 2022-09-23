#PRACTICA MANIPULACION DE ARCHIVOS

#Ejercicio 1:
#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada 
# letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
"""
with open("manipulacion_archivos.txt","r") as archivo:
    linea = archivo.readlines()
    if linea != "p":
       len(linea) 
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
"""       #las utlimas dos 
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
with open("manipulacion_archivos.txt") as archivo:
    lineas = [linea.strip('\n') for linea in archivo.readlines()]
    lista.append(lineas)

print(lista)
"""
"""
lista = []
def guardar(texto, n):
    with open(texto) as archivo:
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


#Ejercicio 6
#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

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

#Ejercicio 9
#Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
#Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con 
#respecto a la cantidad total de palabras.
# VERRRRR
"""
import re
import string
frecuencia = {}
with open("manipulacion_archivos,txt") as archivo:
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