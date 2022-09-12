#Practica manejo de excepciones

#cuestion conceptual, no tan practico. Parcial ejercicio con puntos mas practicos como los del tp

#Ejercicio 1:
"""
lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
try:
    lista_super + "arroz"
except TypeError:
    print("mal usado el +")
except NameError:
    print("no puedo agregar arroz")
finally:
    print("ni idea")
"""

#Ejercicio 2:
#Definir una función que tenga como parámetros una lista de números por un lado y un número por otro 
#y devuelva una lista con la división de cada elemento por el número dado. Por ejemplo, si le paso ([2,4,6,8], 2), 
# debería retornar [1,2,3,4]. Tomar las precauciones necesarias.
"""
lista_numeros = [2,4,6,8]

def division_lista (lista,numero):
    try:
        lista/numero
    except TypeError:
        print("NO puede ser string, lista, diciconario")
    except ZeroDivisionError:
        print("No se puede dividir por cero")

division_lista(lista_numeros,2)
"""

#Ejercicio 3
#Definir un procedimiento, que reciba una lista y un número, el cual tiene que agregar el número a la lista solo 
# si el número es positivo. De lo contrario debería generar un error indicando que el número no es positivo.
"""
lista = [3,5,7,9]

def numero_positivo(lista, numero):
    if numero > 0:
        try:
            lista.append(numero)
        except TypeError:
            print("El numero debe ser positivo")

numero_positivo(lista,-1)

"""