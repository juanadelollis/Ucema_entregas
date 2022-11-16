#Practica de introduccion a python parte 2
 
# Ejercicio 1
"""Cadena = input("Ingrese la palabra: ")
if Cadena[0] == Cadena[0].upper()
print(Cadena)
"""

#Ejercicio 2
"""Numero = int(input("Escriba un numero entero: "))
if Numero == 0:
    print("El numero es cero")
elif Numero >0:
    print("El numero es positivo")
else: "El numero es negativo"

if numero % 2 ==0:
    print("Es par")
else:
    print("Es impar")
"""

#Ejercicio 3 
#Escribí un programa que dado un número del 1 al 6, ingresado por teclado, muestre cuál es el número que está en la 
# cara opuesta de un dado. Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto 
# el número ingresado.
"""Numero = int(input("Escriba un numero: "))
if Numero == 1:
    print("Seis")
elif Numero == 2:
    print("Cinco")
elif Numero == 3:
    print("Cuatro")
elif Numero == 4:
    print("Tres")
elif Numero == 5:
    print("Dos")
elif Numero == 6:
    print("Uno")
elif Numero <1:
    print("El numero es incorrecto ")
elif Numero >6:
    print("El numero es incorrecto ")
"""
""" UNA FORMA MEJOR
numero = int(input("Escribe un numero del 1 al 6: "))
if 1<= numero <= 6:
    if numero == 1:
        print("El numero opuesto es: ", (7 - numero))
    elif numero == 2:
        print("El numero opuesto es: ", (7 - numero))
    elif numero == 3:
        print("El numero opuesto es: ", (7 - numero))
    elif numero == 4:
        print("El numero opuesto es: ", (7 - numero))
    elif numero == 5:
        print("El numero opuesto es: ", (7 - numero))
    elif numero == 6:
        print("El numero opuesto es: ", (7 - numero))
else:
    print("El numero debe estar entre 1 y 6!")
"""

#Ejercicio 4:
"""Paquete = float(input("Cuantos gramos pesa: "))
Pais = (input("Zona de entrega: "))
if Pais == "America del Sur":
    print(Paquete * 10)
elif Pais == "America Central":
    print(Paquete * 15)
elif Pais == "America del Norte":
    print(Paquete * 18)    
elif Pais == "Europa":
    print (Paquete * 24)
elif Pais == "Asia":
    print (Paquete * 30)
elif Pais >5000:
    print("Supera el peso de 5kg, no se transporta ")
"""
""" UNA FORMA MEJOR
paquete = float(input("Escribe el peso en gramos: "))
destino = input("Hacia donde se envia el paquete: ")
if paquete <= 5000:
    if destino == "America del sur":
        print("El costo del envio es: $", paquete * 10)
    elif destino == "America central":
        print("El costo del envio es: $", paquete * 15)
    elif destino == "America del norte":
        print("El costo del envio es: $", paquete * 18)
    elif destino == "Europa":
        print("El costo del envio es: $", paquete * 24)
    elif destino == "Asia":
        print("El costo del envio es: $", paquete * 30)
else:
    print("Por cuestiones de logitica no se transportan paquetes con un peso superior a 5kg")
"""

#Ejercicio 5:
# Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. 
# Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.

"""Dia = int(input("Escriba el numero del dia de la semana: "))
if Dia == 1:
   print("Hoy es Lunes")
elif Dia == 2:
   print("Hoy es Martes")
elif Dia == 3:
   print("Hoy es Miercoles")
elif Dia == 4:
   print("Hoy es Jueves")
elif Dia == 5:
   print("Hoy es Viernes")
elif Dia == 6:
   print("Hoy es Sabado")
elif Dia == 7:
   print("Hoy es Domingo")
   """
""" UNA FORMA MEJOR
numero = int(input("EScribe el numero del dia de la semana: "))
if 1<= numero <= 7:
    if numero == 1:
        print("Hoy es Lunes")
    elif numero == 2:
        print("Hoy es Martes")
    elif numero == 3:
        print("Hoy es Miercoles")
    elif numero == 4:
        print("Hoy es Jueves")
    elif numero == 5:
        print("Hoy es Viernes")
    elif numero == 6:
        print("Hoy es Sabado")
    elif numero == 7:
        print("Hoy es Domingo")
else:
    print("El numero es incorrecto, debe ser entre 1 y 7!")
"""

#Ejercicio 6: 
# Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la lista en otra 
# lista pero en orden inverso, imprimí los elementos de esta última lista.
"""
lista1 = ["marketing", "fundamentos", "analitica", "direccion", "finanzas"]
lista2 = lista1[::-1]
print (lista2)
"""
""" UNA FORMA MEJOR
lista1 = []
lista2 = []

# Recorro la lista1 y leo cada elemento por teclado.
for indice in range(1,6):
	lista1.append(input("Dame la cadena %d:" % indice))
	
# Copio la lista1 en la lista2 en orden inverso
lista2 = lista1[::-1]

# Recorro el vector2 para mostrarlo
for cadena in lista2:
	print(cadena)
"""
"""
lista1 = []
lista2 = []

# Recorro la lista1 y leo cada elemento por teclado.
for i in range(1,6):
	lista1.append(input("Dame la cadena %d:" % i))
	
# Copio la lista1 en la lista2 en orden inverso
lista2 = lista1[::-1]

# Recorro el vector2 para mostrarlo
for i in lista2:
	print(i)

print(lista2)
print(lista1)
"""

#Ejercicio 7:
#Creá un programa que declare una lista y la vaya llenando de números leídos 
# por teclado hasta que se introduzca un número negativo. Una vez hecho esto 
# se deben imprimir los elementos de la lista.
"""
lista = []

def agregar(numero):
    if numero > 0:
      list.append(lista,numero)
    elif numero < 0:
        print(lista)

agregar(5)
agregar(9)
agregar(4)
agregar(-8)
"""
""" UNA FORMA MEJOR
lista = []
numero = int(input("Introduce un número en la lista:"))
while numero>=0:
	lista.append(numero)
	numero = int(input("Introduce un número en la lista:"))

for numero in lista:
	print(numero," ",end="")
"""

#Ejercicio 8 
#Realizá un programa que declare tres listas lista1, lista2 y lista3, donde 
#las dos primeras listas deben tener cinco enteros cada una, ingresados por 
# teclado y asigne para cada elemento de la lista3 la suma de los elementos 
# de la lista1 y la lista2 (es decir, el primer elemento de la lista3 tiene 
# que ser la suma del primer elemento de la lista1 y el primero de la lista2)
"""
lista1 = []
lista2 = []
lista3 = []

for indice in range(1,6):
	lista1.append(int(input("Introduce el elemento %d del vector1: " % indice)))
for indice in range(1,6):
	lista2.append(int(input("Introduce el elemento %d del vector2: " % indice)))

for indice in range(0,5):
	lista3.append(lista1[indice] + lista2[indice])

print("La suma de los vectores es:")
for numero in lista3:
	print(numero," ",end="")
"""

#Ejercicio 9: 
#Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. Se debe introducir el nombre y la edad 
#de cada alumno por teclado. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*). 
#Al finalizar se deben mostrar los siguientes datos:
#- La edad máxima de todos los alumnos.
#- Los alumnos que tengan la edad máxima

"""
nombres = []
edades = []


while True:
    nombre = input("Escribe el nombre de alumno: ")
    if nombre != "*":    
        nombres.append(nombre)
        edades.append(int(input("Escribe la edad del alumno: ")))
    else:
        break

edad_max = max(edades)
print("Alumnos mayores de edad:")

for nombre,edad in zip(nombres,edades):
	if edad >= 18:
		print("-", nombre)

for nombre,edad in zip(nombres,edades):
	if edad == edad_max:
		print("El alumno con la edad maxima es:",nombre)

"""

#Ejercicio 10: 
#Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter 
# en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", 
# el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).

""" 
diccionario = {}
cadena = input("Escribe una cadena:")
for caracter in cadena:
	if caracter in diccionario:
		diccionario[caracter]+=1
	else:
		diccionario[caracter]=1	

for campo,valor in diccionario.items():
	print (campo,"->",valor)
"""

#Ejercicio 11: VEEERRRR
# Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.
""" VEEERRRR
diccionario = {}
cadena = input("Escribe una cadena:")
for caracter in cadena:
	if caracter in diccionario:
		diccionario[caracter]+=1
    elif:
        diccionario[caracter]=1	
    elif:
        diccionario[caracter] = None
        return diccionario[caracter] = 0


for campo,valor in diccionario.items():
    print(campo,"->",valor)
"""

#Ejercicio 12: 
# Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. 
# Cada alumno puede tener distinta cantidad de notas. Guardá la información en un diccionario cuya claves serán 
# los nombres de los alumnos y los valores serán listas con las notas de cada alumno. El programa tiene que pedir el 
# número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo. 
# Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. 
# Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.
"""
alumnos = {}
cantidad = int(input("Introduce la cantidad de alumnos que vamos a guradar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno:")
    notas=[]
    nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    alumnos[alumno] = notas.copy()

for alumno, notas in alumnos.items():
    print("%s ha sacado de nota media %f" % (alumno,sum(notas)/len(notas)))
"""

#FUNCIONES
#Ejercicio 13:
"""
def esmultiplo(numero1,numero2):
	if numero1 % numero2 == 0:
		return True
	else:
		return False

numero1 = int(input("Escriba un numero entero:"))
numero2 = int(input("Escriba otro numero entero:"))

if esmultiplo(numero1,numero2):
	print(numero1,"es múltiplo de",numero2)
else:
	print(numero1,"no es múltiplo de",numero2)
"""
#Ejercicio 14: ver porque dice lo de float, ya estoy usando range???
"""
def tempMedia(Temp1, Temp2):
    return sum(Temp1 + Temp2)/2

cantidad = int(input("Cantidad de dias:"))
for i in range(cantidad):
    Temp_max = float(input("Temperatura maxima: "))
    Temp_min = float(input("Temperatura minima: "))
    print("Temperatura media:", tempMedia(Temp_max, Temp_min))
"""


#Ejercicio 15:
"""
def cargarSocios(socios):
   numero=int(input("Número de socio (0 para cortar): "))
   while numero!=0:
       nombre=input("Nombre y apellido: ")
       fecha=input("Fecha de ingreso (DDMMAAAA): ")
       cuota=input("¿Cuota al día? s/n: ")
       socios[numero]=[nombre,fecha,cuota.lower()=="s"]
       numero=int(input("Número de socio (0 para cortar): "))
   return socios

 
def modificarFecha(socios, fecha_anterior, fecha_nueva):
   for datos in socios.values():
       if datos[1]==fecha_anterior:
           datos[1]=fecha_nueva
   return socios

 
def numeroSocio(socios, nombre):
   for numero,datos in socios.items():
       if datos[0].lower()==nombre.lower():
           return numero
   return 0

 
def formatoFecha(fecha):
   return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

 
def imprimirListado(socios):
   for numero, dato in socios.items():
       print("-Número:",numero)
print("-Nombre:",dato[0])
print("-Ingresó:", formatoFecha(dato[1]))
if dato[2]:
           print("-Cuota al día")
else:
           print("-En deuda")

 
socios_activos={1:["Florencia Ocampo","14092001",True], 2:["David Estévez","14092001",True], 3:["Sofía Cáceres","14092001",True]}

 
print("***Cargar socios")
socios_activos=cargarSocios(socios_activos)

 
print("El club tiene", len(socios_activos), "socios")

 
print("***Registrar pago de cuotas")
numero=int(input("Número de socio: "))
socios_activos[numero][2]=True

 
print("***Modificando fecha de ingreso...")
socios_activos=modificarFecha(socios_activos, "21102017", "22102017")

 
print("***Eliminar socio")
nombre=input("Nombre y apellido: ")
numero=numeroSocio(socios_activos, nombre)
if numero in socios_activos:
    del socios_activos[numero]

 
imprimirListado(socios_activos)
"""

