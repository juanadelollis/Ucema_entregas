#Practica expresiones regualres

#Ejercicio 1
#Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
"""
import re

frase = "fewnlnfklwekfnlew"

def caracteres_permitidos(string):
    return not bool(re.search("[a-zA-Z0-9]"), string)

caracteres_permitidos(frase)
"""
#Ejercicio 2
#mismo que el 1

#Ejercicio 3
"""
import re
patron = "he*"

def encontrar_patron(string):
    if re.search(patron,string) is not None:
        return "se encontro patron"
    else:
        return "no se encontró patron"

print(encontrar_patron("hello"))
"""
"""
import re
patron = "he+"

def encontrar_patron(string):
    if re.search(patron,string) is not None:
        return "se encontro patron"
    else:
        return "no se encontró patron"

print(encontrar_patron("hello hello"))
"""
"""
import re
patron = "he{2,3}"

def encontrar_patron(string):
    if re.search(patron,string) is not None:
        return "se encontro patron"
    else:
        return "no se encontró patron"

print(encontrar_patron("heeeelloo"))
"""

#Ejercicio 4
#Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado 
#(el string no debe contener espacios).
"""
import re
def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "patrón encontrado"
    else:
        return "patron no encontrado"

print(palabras_unidas("snsjskkcjbdlkj"))
"""

#Ejercicio 5
#Escribí un programa que diga si un string empieza con un número específico.
"""
import re

string = input("Escribe el string en el que quieres buscar: ")
patron = input("Escribe el numero a buscar: ")
patron = "^" + patron

def empieza_numero(string,patron):
    if re.match(patron,string) is not None:
        return "patrón encontrado"
    else:
        return "patron no encontrado"

print(empieza_numero(string,patron))
"""
#Ejercicio 6
#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.
"""
import re

def encontrar_frase(frase_dada, lista_string):
    for string in lista_string:
        respuesta = re.search(frase_dada, string)
        if bool(respuesta):
            print("Encontre el string " + frase_dada + " en el texto")
        else: 
            print("No encontre nada")

lista =["buenos dias", "buenas noches", "tarde"]  
frase = input("Escriba la palabra que quiere encontrar: ")

encontrar_frase(frase, lista)
"""

#Ejercicio 7
#Realizá un programa que encuentre un string que contenga 
#solamente letras minúsculas, mayúsculas, espacios y números
"""
import re

cadena = input("Escriba una frase: ")

def encontrar_string(string):
    patron = "^[a-zA-Z0-9\s]+"
    if re.search(patron,string) is not None:
        return "Se encontro el patron"
    else:
        return "No se cumple el patron"

print(encontrar_string(cadena))
"""

#Ejercicio 8
#Escribí un programa que separe y devuelva los caracteres númericos de un string.

#LA FUNCION SPLIT SACA DEL STRING EL PATRON Y TE DEVUELVE LO QUE QUEDA

"""
import re

string = input("Escriba una frase: ")

def separar_funciones(string):
    patron = "\D+" #ningun digito
    lista_numeros = re.split(patron, string, flags=re.IGNORECASE)
    print(lista_numeros)

separar_funciones(string)
"""

#Ejercicio 9
#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
# (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
"""
import re

string =("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")

def extraer_guiones(string):
    patron = "-(.*?)-"
    lista_guiones = re.findall(patron, string)
    print(lista_guiones)

extraer_guiones(string)
"""

#Ejercicio 10
#Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings 
#están delimitadas por los caracteres @ o &.
""" 
import re

string = input("Escriba un string: ")

def extraer_subtring(string):
    patron = "@(.*?)&"
    busqueda = re.findall(patron, string)
    print(busqueda)
    for item in busqueda:
        print("La posicion del substring es: ", string.find(item))

extraer_subtring(string)
"""

"""
import re

string = input("Escriba un string: ")

found = re.search("@(.*?)&", string).group()
print(found)
print("La posicion del substring es: ",string.index(found))
"""
#Ejercicio 11
#Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string 
#empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"])

"""
import re

lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]

def empieza_con(lista):
    for i in lista:
        frase = re.match("(P\w+)\W(P\w+)", i)
        if frase:
            print(frase.groups())

empieza_con(lista)
"""    
#Ejercicio 12
#Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos 
#por la barra vertical (|).
""" 
import re

cadena = input("Escriba un string: ")

def remover_espacios(string):
    patron = "[_\s:]"
    frase = re.sub(patron, "(|)", string)
    print(frase)

remover_espacios(cadena)
"""
#Ejercicio 13
#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
"""
import re

cadena = input("Escriba un string: ")

def guiones_bajos(string):
    patron = "\W" #--> negacion del alfanumerico
    frase = re.sub(patron, "_", string, 2)
    print(frase)

guiones_bajos(cadena)
"""

#Ejercicio 14
#Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.
"""  
import re

cadena = input("Escriba un string: ")

def punto_coma(string):
    patron = "[\s\t]"
    frase = re.sub(patron, ";", string)
    print(frase)

punto_coma(cadena)
"""
#Ejercicio 15
#Realizá un programa que validar si una cuenta de mail está escrita correctamente.
"""
import re

mail = input("Escriba su mail: ")

def validar_mail(email):
    patron = '^[a-z0-9]+[\._]*?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(patron, email)):
        print("Mail valido")   
    else:  
        print("Mail invalido") 

validar_mail(mail)
"""
