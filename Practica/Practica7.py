
import requests

pikachu = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

with open("ficha_tecnica_pokemon.txt", "a") as salida:
    salida.write(str(pikachu.json()))

#PRACTICA REQUESTS

import requests 

# DESAFIO 1:
# En base al siguiente enlace "https://pokeapi.co/api/v2/pokemon/pikachu", realizar las siguientes actividades 
# adjuntando los archivos resultantes y el código utilizado para la realización de cada paso:

#a) ¿Cuál es el dominio al que estamos consultando?
"""
pokeapi.co
"""
# b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type? Obtené la información correspondiente al campo "forms".
"""
>>>r = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
>>> r.status_code
>>>200
"""
 
#c) Averigüá cuántos Pokemones almacena la API.
"""
>>> r = requests.get("https://pokeapi.co/api/v2/pokemon")
>>> len(r.json())
4
→ de la forma de arriba no funciona por como esta hecha la api, est separada en grupitos
"""

#d) ¿Cómo esperás que sea la URL para obtener las habilidades de los Pokemons (abilities)? ¿y cómo será la url para obtener la información sobre la habilidad 2?
"""
"https://pokeapi.co/api/v2/abilities"
"https://pokeapi.co/api/v2/abilities?habilidad=2" o "https://pokeapi.co/api/v2/abilities2"
mientras tenga lógica lo que estás haciendo está bien:
/abilities2 → bien
/abilities/2 → si pongo la barra sale de la rama de habilidades
"""
#f) Guardar los datos correspondientes a Pikachu y Sylveon en un archivo de nombre "ficha_tecnica_pokemon.txt".
"""
>>> with open ("ficha_tecnica_pokemon.txt", "a") as salida:
        salida.write(string(r.json()))
229451

si nos pide algo en especial y no todo tenemos que especificar el campo desde el json()
"""
#g) Describí la arquitectura cliente-servidor y los roles de cada parte

#🧗‍♀️ Desafío II Dado el siguiente enlace "https://jsonplaceholder.typicode.com/todos", 
# realizar las siguientes actividades adjuntando los archivos resultantes y el código utilizado para la realización 
# de cada paso:

#a) ¿Cuál es el dominio al que estamos consultando?
"""
jsonplaceholder.typicode.com
"""
#b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type?
"""
import requests
r = requests.get("https://jsonplaceholder.typicode.com/todos")
r.status_code
"""
#c) Modificar el contenido cuyo UserId es 1 y su id es 2 con un nuevo título e indicando que está completo (comleted).

#d) En la arquitectura cliente-servidor ¿Qué características tiene el cliente?