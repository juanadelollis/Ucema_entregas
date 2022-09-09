#Expresiones regulares
# Ejercicio 1
#Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

import re

frase = "fewnlnfklwekfnlew"

def caracteres_permitidos(string):
    return bool(re.search("[a-zA-Z0-9]"), string)

caracteres_permitidos(frase)



#Ejercicio 6
#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.
""" listaStrings = ["unstring", "otro", "otromas"]
def ej6(listaStr): """

    




#Ejercicio 7
#Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números