#Resolucion guia Intro_Python

#Desafío I: ¿Qué pasos nos faltaron? ¿Podes pensar otras posibles situaciones que no estemos contemplando 
#(como por ejemplo que no haya yerba en el yerbero)? Agregá a la guía para preparar mate(script) los pasos, 
#problemas posibles y las soluciones que se te ocurran en sentencias u ordenes sencillas (ejemplo; verificar 
#si hay yerba en el yerbero. Si no hay agregar, si hay llenar el mate)

##NO SE SI ESTA BIEN LA ALINEACION##
"""Paso 1) Seleccionar el mate

Paso 2) Buscar el yerbero

Paso 3) Buscar el termo

Paso 4) Clentar el agua

Paso 5) Verificar que el yerbero esta lleno:

    Moemento decisivo:

        Paso 6) Si el yerbero esta vacio, llenarlo.

        Paso 7) Si el yerbero esta lleno:

             Paso 8) Verificar si el mate está vacío: 

                  Momento decisivo:

                    Paso 9) Si el mate está vacío, llenarlo con la yerba del yerbero.

                    Paso 10) Si el mate está lleno:

                         Paso 11) Vaciarlo en una maceta

                         Paso 12) Llenarlo con la yerba del yerbero."""

#Para pensar 🤔: 
"""¿Y cómo te parece que funciona tu teléfono celular 📱?
Funciona de igual manera que la computadora, es decir, tiene un hardware y un software.
"""

#🧗‍♀️ Desafío II: falta consigna

"""El prompt de Python es >>>, mientras que el de Visual code es $.
La terminal visual code entiende el lenguaje python""" ##Consultar##

#NO PUEDO HACER EL PRINT## me tira un syntax error near unexpected token

"""Para pensar 🤔:¿Cuál es el resultado? ¿Qué significa entonces el *? 
Para pensar 🤔:¿Cuál es el resultado? ¿Qué significa entonces el /?
#>>> 3*5
15  
#>>> 8/4
2.0
"""
#Para pensar 🤔:¿Cuál es el resultado? ¿Qué tipo de dato es?
  #>>> Edad_lola = 13
  #>>> Edad_ana = 32
  #>>> Edad_ana == Edad_lola
#False

#Para pensar 🤔:¿Qué resultado nos da? ¿Por qué?
#>>> afirmacion = "si"
#>>> Gran_afirmacion = "SI"
#>>> Gran_afirmacion == afirmacion
#True

#Para pensar 🤔:¿Posición tendrá la letra "C' en el string "Marie Curie"? ¿Por qué?
"""" Va a tener adignado la posicion 6 porque el caracter "c" esta en la posicion 6 del string"""

#Para pensar 🤔:¿Qué resultado nos dá el código anterior? ¿Por qué? 
#¿Qué pasa si removemos el último número (hacemos saludo[0:])?
""" Saludo = "Hola mundo" 
#>>> Saludo[0]
'H'
#>>> Saludo[0:3]
'Hol'
#>>> Saludo[0:]
'Hola mundo'
"""

#🧗‍♀️ Desafío III: Probá las lineas anteriores y anotate para qué sirve cada uno de los métodos y funciones.
#Len es para coontar el largo del string, cuanot caracteres lo componen
#upper es para poner todo en mayuscula, lower para poner todo en minuscula
#Count es para countar algo, como la cantidad de 'o' que tiene el string
#Replace es para cambiar un caracter por otro en el string

"""
#>>> len(Saludo)
10
#>>> Saludo.upper()
'HOLA MUNDO'
#>>> Saludo.lower()
'hola mundo'
#>>> Saludo.count('o')
2
#>>> Saludo.replace('o','a')
'Hala munda'
"""
#Para pensar 🤔: ¿Se podrán combinar los métodos? Probá hacer saludo.upper().lower() ¿Qué dá? ¿Por qué?
""" 
#>>> Saludo.upper().lower()
'hola mundo
 """
 #Da lo que dice la ultima funcion, creo que es porq son contradictorias


 #🧗‍♀️ Desafío IV: Vimos que el método replace nos permite reemplazar un caracter por otro de un string dado, 
 #pero nos dejará reemplazar un segemento más largo? Probá hacer saludo.replace("mundo", "terricolas")
"""#>>> Saludo.replace("mundo", "terricolas")
'Hola terricolas'
"""

#Para pensar 🤔: ¿Si imprimís saludo luego de ejecutar la linea anterior qué obtenés? 
#¿Cambió el valor de la variable?
"""" >>> Saludo
'Hola mundo'
No cambio el valor de la variable"""

#Para pensar 🤔: ¿Cómo podrías conocer la longitud de la lista?
"""
#>>> len(lista)
3
"""
#Para pensar 🤔: Probá la sentencia lista.index('25') ¿Qué resultado obtenes? ¿Para qué sirve index()
   #>>> lista.append('25')
   #>>> lista.remove('25')
   #>>> lista.index('25')
   #Traceback (most recent call last):
   #  File "<stdin>", line 1, in <module>
   #ValueError: '25' is not in list
   #>>> lista
   #[2, 5, 4]
   #>>> lista.index('5')
   #Traceback (most recent call last):
   # File "<stdin>", line 1, in <module>
   #ValueError: '5' is not in list
   #>>> lista.index(5)
   #1
"""index te dice en que posicion esta en al lista""" #VER

#Para pensar 🤔: ¿Cómo harías para obtener todos los valores de un diccionario? 
""" Ver como se hace, no entendi lo de las llaves y los diccionarios"""

#diccionario = {"llave": "valor"}
#diccionario.values

#🧗‍♀️ Desafío VI: Después de tanto programar necesitamos unos matecitos. Hoy aprendiste a prepararlos. 
#Lo que no estoy segura es de que el agua alcance para toda la ronda. Suponiendo que cada cebada de mate 
#consume del 30 ml de agua. Cosntruí una función que nos permita calcular cuántos termos de 1000 ml llenos 
#consumiremos para un ronda dada (es decir una cantidad de personas dada).

#cantidad = 4
#def cantidad_termos(numero):
#      resultado = (30*cantidad)/1000
#      return resultado

#🧗‍♀️ Desafío VII: Siempre con los mates, vienen bien unas facturitas 🥐🥐
#¿Si hacemos una vaquita ? Vaquita se le dice en Argentina a hacer una colecta de plata para un fin común. 
#Creá función que nos permita dividir los costos de una docena de facturas entre cierta cantidad de comensales.
"""def vaquita(5):
    resultado = 
    return resultado"""


#🧗‍♀️ Desafío VIII: En una ronda pequña de mate 🧉 no hace falta llenar tooooodo el termo, con un poco 
# de agua quizás alcanza. Definí una función calcular_cantidad_de_agua que espere una cantidad de personas 
# como argumento y devuelva la cantidad de mililitros con los que tenemos que cargar el termo.

#👀 ¡OJO! Si llega a 1000 debería retornar la advertencia "vas a necesitar más de un térmo"

"""def calcular_cantidad_de_agua(numero):
  resultado = (numero*200)
  if resultado < 1000:
     "Vas a necesitar", resultado
  else: 
    "Vas a necesitar mas de un termo"
"""

pedido = dict ["Ana" : "no veggie", "Paul": "veganas", "Luz": "vegetarianas" ]

