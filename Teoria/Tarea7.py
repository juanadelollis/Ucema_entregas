
#--------14/10 Clase 12: HTTP Y REST
"""
El camino hacia los recursos de manera local es el path → donde tenía mi recurso localmente
Pero en la web el concepto análogo es la URL, la diferencia es que la ruta no te lleva a un recursos local en tu máquina, sino que te lleva a otra máquina en algún lugar del mundo. Es un localizador, un path al que accedo en la web.

"""
#🤔 Para pensar: ¿a qué corresponde cada parte de una URL?

#Las podemos caracterizar de distintas formas: 
# - https://: la primera parte de la URL, se corresponde con el tipo de protocolo de comunicación que voy a tener que usar para poder dialogar con esa aplicación/servidor. La “s” es de secure, usa http pero es más segura, se valida y auténtica datos del usuario.
# - docs.google.com: la segunda parte es el dominio, es el seudónimo, una forma amigable de decir la IP, la localización exacta de esa maquina(identificados) en al cual esta alocado el archivo o recurso que estás consultando. Estos dominios se compran.
# - document: la última parte, es el recurso al que estoy consultando. Es directo, pero si es una aplicación puede haber muchas más.

"""
pip install requests

import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas/1')
r.json()
{
  "id": 1,
  "tipo": "pantalon",
  "talle": 35
}
"""

#🤔 Para pensar: ¿Qué características tiene este formato? ¿Qué tipo de datos puede soportar? ¿por qué devolver JSON? 
# ¿Quién puede leerlo? ¿A quién le sirve?
"""
import requests
url = "https://macowins-server.herokuapp.com/prendas/1"
respuesta = requests.get(url)                                               
>>> respuesta
<Response [200]> 
hicimos el pedido, le preguntaste y te respondio 200
en web todo tiene un código asociado
la respuesta no es legible, por eso vamos a buscar un formato que nosotros podemos interpretar → ese formato es json (texto plano, estructurado de forma intuitiva), tiene una clave y podes acceder a los valores.

>>> respuesta.json()
{'id': 1, 'tipo': 'pantalon', 'talle': 35}

#get: es un verbo http que sirve para hacer pedidos al servidor, trae información
#.json: estoy estructurando esos datos en un término legible para los humanos, es como un diccionario. Es un formato de datos.
"""

#🏅 DESAFIO I: Hacé otro pedido para traer a la prenda 20. Deberías obtener el siguiente resultado:
"""
import requests

r = requests.get('https://macowins-server.herokuapp.com/prendas/20')
print(r.json())

# devuelve: {'id': 20, 'tipo': 'saco', 'talle': 'XL'}
"""

# 🏅 Desafío II: ¡averigualo! Hacé requests.get('https://macowins-server.herokuapp.com/prendas/400')
"""
import requests

r = requests.get('https://macowins-server.herokuapp.com/prendas/400')
print(r.json())
"""

#HEADERS  
"""
r_all.headers  
{'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'application/json; charset=utf-8', 'Etag': 'W/"569-0xEKDv5V6Jh+M2gEXFu7RElZ/+c"', 'Vary': 'Accept-Encoding', 'Content-Encoding': 'gzip', 'Date': 'Fri, 14 Oct 2022 13:00:25 GMT', 'Transfer-Encoding': 'chunked', 'Via': '1.1 vegur'}"""
#STATUS
"""
r_all.status_code
200

SERVIDOR → siempre manda el recurso que se pidió en el formato deseado y un código que le dice al cliente si la 
comunicación funcionó o no.

Que quiere decir ese código?
código 404 → no encuentra, not found
el código ya te dice si funciono, como se establece la comunicación y que paso. El servidor puede estar caído, 
puede ser que busque y no lo encontró. Cada código dice cómo funcionó la comunicación.
código 200 → OK

quien dice que codigo va → el que desarrollo el software, el que tomo la decision

"""
#✍️ Autoevaluación: ¿Para qué sirve el método headers? ¿Que nos permitió?
""" 
Headers → obtengo toda la información de la comunicación
"""
 # Desafío III: contrastá con lo que sucede al hacer get de 'https://macowins-server.herokuapp.com/prendas/1' 
# ¿Qué te devuelve el método headers? ¿Qué status_code obtenes?
"""
  >>> import requests
  >>> r = requests.get('https://macowins-server.herokuapp.com/prendas/400')
  >>> r.headers

{'Server': 'Cowboy', 
'Connection': 'keep-alive', 
'X-Powered-By': 'Express', 
'Expires': '-1', 
'Content-Type': 'application/json; charset=utf-8', 
'Content-Length': '50', 
'Etag': 'W/"32-i8e+gZ5GUBVXp/2hTq5pj1i9+f8"', 
'Vary': 'Accept-Encoding', 'Date': 'Sat, 27 Feb 2021 18:11:12 GMT',
'Via': '1.1 vegur'}

Da información : a donde se conectó (servidor, cowboy), cómo funcionó la conexión (connection),  
fecha en la que se hizo la conexión, content type: el formato de texto con el cual me dieron la respuesta, 
que tipo de caracteres usa (utf8 es el más común).
El content type y la fecha en la cual se hizo la conexión → va a variar el content type en función de lo que 
queremos entregarle al cliente. Lo decide el desarrollador en base  a lo que se necesita mostrar al cliente.

>>> r_all.status_code
200

"""
#✍️ Autoevaluación: ¿qué representa el código 500? ¿Por qué tenemos que hacer r.contents además de r.headers? 
# ¿Qué partes puede tener un mensaje HTTP? ¿Qué partes deben estar presentes y cuáles no? ¿En qué casos?

#🤔 Para pensar: ¿es lo mismo consultar /prendas/ que /prendas/1? ¿En qué se diferencian? ¿Qué ocurre si hacemos 
# r.content? ¿Por qué?
"""
Un parámetro hace uso de las características de un recurso → el /1 es el id
Puedo ser mucho más específico sobre lo que quiero buscar. Las características de las prendas son tipo y talle.

"""

#🏅 Desafío V: hacé requests.get('https://macowins-server.herokuapp.com/ventas') y 
# requests.get('https://macowins-server.herokuapp.com/ventas/2)' y contrastá el resultado con tu respuesta anterior

"""
/ventas: trae todas las ventas de Makowins

/ventas/2: trae la segunda venta, als especificaciones solo de esa
"""

#✍️ Autoevaluación: ¿qué acabamos de hacer? ¿para qué nos sirvió el ?...=...?
"""
recurso ? nombre de la característica = lo que quieras
? → ahora te voy a especificar cosas, filtros para hacer en la base de datos

>>> r_1 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=pantalon")
>>> r_1.json()
[{'id': 1, 'tipo': 'pantalon', 'talle': 35}, {'id': 2, 'tipo': 'pantalon', 'talle': 36}, {'id': 3, 'tipo': 'pantalon', 'talle': 37}, {'id': 4, 'tipo': 'pantalon', 'talle': 38}, {'id': 5, 'tipo': 'pantalon', 'talle': 39}, {'id': 6, 'tipo': 'pantalon', 'talle': 40}, {'id': 7, 'tipo': 'pantalon', 'talle': 41}, {'id': 8, 'tipo': 'pantalon', 'talle': 42}, {'id': 9, 'tipo': 'pantalon', 'talle': 43}, {'id': 10, 'tipo': 'pantalon', 'talle': 44}]
>>> r_1 = requests.get("https://macowins-server.herokuapp.com/prendas?talle=l")      
>>> r_1.json()
[]
>>> r_1 = requests.get("https://macowins-server.herokuapp.com/prendas?talle=L")  
>>> r_1.json()
[{'id': 14, 'tipo': 'remera', 'talle': 'L'}, {'id': 19, 'tipo': 'saco', 'talle': 'L'}]

& → para especificar que filtras más veces

>>> r_1 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=pantalon&talle=L")
>>> r_1.json()
[]
>>> r_1 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=pantalon&talle=42")
>>> r_1.json()
[{'id': 8, 'tipo': 'pantalon', 'talle': 42}]
"""

#🏅 Desafío VI: Obtené las remeras.
""" 
import requests
r_1 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=remera")
r_1.json()
"""

#🏅 Desafío VII: Obtené las remeras XS
"""
r_1 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=remera&talle=XS")
r_1.json()
"""

#✍️ Autoevaluación: ¿Para qué sirven los parámetros?
"""
Un parámetro hace uso de las características de un recurso → el /1 es el id
Puedo ser mucho más específico sobre lo que quiero buscar. Las características de las prendas son tipo y talle.

"""





#APUNTES DE CLASE
#lo podemos hacer en el interprete o en el script
""" con el servidor tenemos que hablar civilizadamente --> protoclo http
request es un biblioteca que te permite hacer comunicaciones en http
necesitamos importar la biblioteca
"""
#import requests

#vamos a hacerle un pedido al servidor
# Podemos pedirle que nos diga que elementos tiene la web


#url = "https://macowins-server.herokuapp.com/prendas/1"
"""
las pruebitas las haces en la terminal y el resto lo haces en python

>>> import requests
>>> url = "https://macowins-server.herokuapp.com/prendas/1"
>>> respuesta = requests.get(url)                                               
>>> respuesta
<Response [200]>
>>> respuesta.json()
{'id': 1, 'tipo': 'pantalon', 'talle': 35}
>>> respuesta.json()["id"]
1
>>> r_all = requests.get("https://macowins-server.herokuapp.com/prendas")      
>>> r_all.json()
[{'id': 1, 'tipo': 'pantalon', 'talle': 35}, {'id': 2, 'tipo': 'pantalon', 'talle': 36}, {'id': 3, 'tipo': 'pantalon', 'talle': 37}, {'id': 4, 'tipo': 'pantalon', 'talle': 38}, {'id': 5, 'tipo': 'pantalon', 'talle': 39}, {'id': 6, 'tipo': 'pantalon', 'talle': 40}, {'id': 7, 'tipo': 'pantalon', 'talle': 41}, {'id': 8, 'tipo': 'pantalon', 'talle': 42}, {'id': 9, 'tipo': 'pantalon', 'talle': 43}, {'id': 10, 'tipo': 'pantalon', 'talle': 44}, {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, {'id': 12, 'tipo': 'remera', 'talle': 'S'}, {'id': 13, 'tipo': 'remera', 'talle': 'M'}, {'id': 14, 'tipo': 'remera', 'talle': 'L'}, {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, {'id': 17, 'tipo': 'saco', 'talle': 'S'}, {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, {'id': 19, 'tipo': 'saco', 'talle': 'L'}, {'id': 20, 'tipo': 'saco', 'talle': 'XL'}, {'tipo': 'chomba', 'talle': 'XS', 'id': 21}, {'tipo': 'chomba', 'talle': 'XS', 'id': 22}]    
>>> r_all.headers  
{'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'application/json; charset=utf-8', 'Etag': 'W/"569-0xEKDv5V6Jh+M2gEXFu7RElZ/+c"', 'Vary': 'Accept-Encoding', 'Content-Encoding': 'gzip', 'Date': 'Fri, 14 Oct 2022 13:00:25 GMT', 'Transfer-Encoding': 'chunked', 'Via': '1.1 vegur'}
>>> r_all.status_code
200
>>> len(r.json())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'r' is not defined
>>> len(respuesta.json())
3
>>> len(r_all.json())
22
>>> r_1 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=pantalon")
>>> r_1.json()
[{'id': 1, 'tipo': 'pantalon', 'talle': 35}, {'id': 2, 'tipo': 'pantalon', 'talle': 36}, {'id': 3, 'tipo': 'pantalon', 'talle': 37}, {'id': 4, 'tipo': 'pantalon', 'talle': 38}, {'id': 5, 'tipo': 'pantalon', 'talle': 39}, {'id': 6, 'tipo': 'pantalon', 'talle': 40}, {'id': 7, 'tipo': 'pantalon', 'talle': 41}, {'id': 8, 'tipo': 'pantalon', 'talle': 42}, {'id': 9, 'tipo': 'pantalon', 'talle': 43}, {'id': 10, 'tipo': 'pantalon', 'talle': 44}]
>>> r_1 = requests.get("https://macowins-server.herokuapp.com/prendas?talle=l")      
>>> r_1.json()
[]
>>> r_1 = requests.get("https://macowins-server.herokuapp.com/prendas?talle=L")  
>>> r_1.json()
[{'id': 14, 'tipo': 'remera', 'talle': 'L'}, {'id': 19, 'tipo': 'saco', 'talle': 'L'}]
>>> r_1 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=pantalon&talle=L")
>>> r_1.json()
[]
>>> r_1 = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=pantalon&talle=42")
>>> r_1.json()
[{'id': 8, 'tipo': 'pantalon', 'talle': 42}]
"""