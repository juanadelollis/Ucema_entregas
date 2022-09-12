#Manejo de excepciones

#🧗‍♀️Desafio I: Descargá y ejecutá el script1_manejo_errores.py

#Para pensar 🤔: ¿Qué tipo de error se obtiene al ejecutar el programa? 
# ¿En dónde se encuentra el error? ¿Cómo te das cuenta?

"""
Excepcion: Te da --> ZeroDivisionError: complex division by zero.
Syntax error: Tambien falta uno de los parentesis.
Te das cuenta porque te aparece el ^.
Anticipación de los errores, tratamos de hacer que rompa a proposito para arreglarlo. 
Ejemplo: Si D te da un valor negativo y si A te da cero --> no se puede
Una opción es poner un if,pero no esta bueno. Conviene hacer un try 
"""

#Para pensar 🤔: ¿Qué nos dice el mensaje de excepción? ¿Qué es la excepción de nombre?
"""Nos dice que no esta definido divisor, y eso es una excepcion de nombre"""

#Para pensar 🤔: ¿Qué nos dice el último mensaje de excepción? ¿Qué es la excepción de tipo?
"""Nos dice que no se puede sumar un entero y un string, es una excepcion de tipo"""


#🧗‍♀️Desafio II: Creá una función denominada mitades que tenga como argumento un número e imprima el resultado 
# de la división de ese número por 2
"""
def mitades(numero):
      return(numero/2)

print(mitades(9))
print(mitades(0))
"""

#Para pensar 🤔: ¿Qué crees que ocurrirá cuando ingresas un 9 como parámetro? ¿Y con un 0?
"""Da estos resultados: 
4.5
0.0
"""
#🧗‍♀️Desafio III: ¿Cómo mejorarías tu función para que sea capaz de manejar el error de la división por cero? 
# Reescribí la función incorporando una declaración try-except
"""
def mitades(numero):
      return(numero/2)
   except ZeroDivisionError:
        print("No se puede dividir por 0")

print(mitades(9))
print(mitades(0))
"""

