#CIENCIA DE DATOS

#Introducción a la ciencia de datos - Pandas

import pandas as pd
#Ejercicio 1
#Escribí un programa que sume, reste, multiplique y divida dos series de números de Pandas.
"""
serie1 = pd.Series([3, 7, 12, 15, 21])
serie2 = pd.Series([1, 4, 10, 14, 19])

print("Sumar:")
print(serie1 + serie2)
print("Restar:")
print(serie1 - serie2)
print("Multiplicacion:")
print(serie1 * serie2)
print("Division:")
print(serie1/serie2)

"""
""" DEVUELVE ESTO:
Sumar:
0     4
1    11
2    22
3    29
4    40
dtype: int64
Restar:
0    2
1    3
2    2
3    1
4    2
dtype: int64
Multiplicacion:
0      3
1     28
2    120
3    210
4    399
dtype: int64
Division:
0    3.000000
1    1.750000
2    1.200000
3    1.071429
4    1.105263
dtype: float64
"""

#Ejercicio 2
#Realizá un programa que compare (si son mayores, menores o iguales) los elementos de dos series de números de Pandas.
"""            
serie1 = pd.Series([3, 7, 12, 15, 21])
serie2 = pd.Series([1, 4, 10, 14, 19])

print("Serie 1 es mayor a serie 2:")
print(serie1 > serie2)
print("Serie 1 es menor a serie 2:")
print(serie1 < serie2)
print("Serie 1 es igual a serie 2:")
print(serie1 == serie2)

DEVUELVE ESTO   
Serie 1 es mayor a serie 2:
0    True
1    True
2    True
3    True
4    True
dtype: bool
Serie 1 es menor a serie 2:
0    False
1    False
2    False
3    False
4    False
dtype: bool
Serie 1 es igual a serie 2:
0    False
1    False
2    False
3    False
4    False
dtype: bool
"""

#Ejercicio 3
#Escribí un programa para convertir un diccionario a una serie de Pandas.
"""
dict1 = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
df = pd.DataFrame(dict1)
#serie = pd.Series(df)
print(df)
"""
#Ejercicio 4
#Escribí un programa que dado un diccionario cuyos valores son listas de números, cree otro diccionario con las 
#mismas claves, pero donde los valores sean una lista de números donde se potencia un número por el siguiente, 
# tomándolos de a pares. Para ser más claros miremos este ejemplo donde si un diccionario es:

#Ejercicio 5
#Realizá un programa para crear y mostrar un DataFrame a partir de un diccionario y de unas etiquetas (o labels).
"""
datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(data= datos_ejemplo, index= labels)
print(df)
"""
""" DEVUELVE ESTO:
     nombre  puntaje  intentos  califica
a  Agustina     12.5         1         1
b     Diana      9.0         3         0
c     Karen     16.5         2         1
d    Julián     13.0         3         0
e    Emilio      9.0         2         0
f    Miguel     20.0         3         1
g     Mateo     14.5         1         1
h     Laura     10.0         1         0
i     Jorge      8.0         2         0
j     Lucas     19.0         1         1
"""

#Ejercicio 6
#Escribí un programa que muestre un resumen de la información básica de un DataFrame y sus datos.
"""
datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(data= datos_ejemplo, index= labels)

df.info()
"""
""" Devuelve esto, se podia usar describe peroe so es mas estadistico
Index: 10 entries, a to j
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   nombre    10 non-null     object
 1   puntaje   10 non-null     float64
 2   intentos  10 non-null     int64
 3   califica  10 non-null     int64
"""

#Ejercicio 7
#Escribí un programa que obtenga las 3 primeras filas de un DataFrame dado.
"""
datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(data= datos_ejemplo, index= labels)

print(df.head(n=3))
"""
"""DEVUELVE ESTO
     nombre  puntaje  intentos  califica
a  Agustina     12.5         1         1
b     Diana      9.0         3         0
c     Karen     16.5         2         1
"""
#Ejercicio 8
#Realizá un programa que seleccione e impirma las columnas "nombre" y "puntaje" del DataFrama anterior.
"""
datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(data= datos_ejemplo, index= labels)

print(df[["nombre","puntaje"]])
"""
#NOMBRE DEL DATAFRAME Y ENTRE CORCHETES LA LISTA DE LAS COLUMNAS --> DF[COLUMNAS]
#PERO COMO LA LISTA TAMBIEN LLEVA EL NOMBRE DE LAS COLUMNAS EN CORCHETES --> COLUMNAS = ["NOMBRE", "PUNTAJE"]
"""DEVUELVE ESTO:
     nombre  puntaje
a  Agustina     12.5
b     Diana      9.0
c     Karen     16.5
d    Julián     13.0
e    Emilio      9.0
f    Miguel     20.0
g     Mateo     14.5
h     Laura     10.0
i     Jorge      8.0
j     Lucas     19.0
"""

#Ejercicio 9
#Escribí un programa que dado el DataFrame anterior imprima los nombres en mayúscula y la longitud de los mismos 
#en una nueva tabla.
"""
datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(data= datos_ejemplo, index= labels)

new_dict = {}

for nombre in df["nombres"]:

"""
