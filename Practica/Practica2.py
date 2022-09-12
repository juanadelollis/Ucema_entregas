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
"""

#Ejercicio 3
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

#Ejercicio 5:
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
#Ejercicio 6:
"""
lista1 = ["marketing", "fundamentos", "analitica", "direccion", "finanzas"]
lista2 = list(lista1)
print (lista2)
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
#Ejercicio 8 -----------------VER
#Realizá un programa que declare tres listas lista1, lista2 y lista3, donde 
#las dos primeras listas deben tener cinco enteros cada una, ingresados por 
# teclado y asigne para cada elemento de la lista3 la suma de los elementos 
# de la lista1 y la lista2 (es decir, el primer elemento de la lista3 tiene 
# que ser la suma del primer elemento de la lista1 y el primero de la lista2)
"""
lista1 = [4,6,3,5,7]
lista2 = [7,2,4,6,3]
lista3 = []

for i in lista1:
    lista3.append(lista1[i])

for i in lista2:
    lista3[i] = lista3[i] + lista2[i]

print(lista3)

"""
#Ejercicio 9: VERRRRR
"""
alumnos = []

def nombres(nombre, edad):
    if nombre != "*":
      list.append(alumnos,nombres)
    elif nombre == "*":
        print(max(edad))
        print()

nombres("maria",19)
nombres("juan",24)
nombres("tomas",25)
nombres("*",18)
"""

#Ejercicio 10: 

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
"""

diccionario = {}
cadena = input("Escribe una cadena:")
for caracter in cadena:
	if caracter in diccionario:
		diccionario[caracter]+=1
    elif:
        diccionario[caracter]=0	
    elif:
        diccionario[caracter]=1	

for campo,valor in diccionario.items():
    print(campo,"->",valor)
"""

#Ejercicio 12:
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
    Temp1 = float(input("Temperatura maxima: "))
    Temp2 = float(input("Temperatura minima: "))
    print(tempMedia(Temp1, Temp2))

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