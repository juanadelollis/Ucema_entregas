#-----4/11 Clase 15: maquetado y ciencia de datos

#--- MAQUETADO
#🧗🏻‍♀️ Desafio I: Buscá qué otras etiquetas existen y para qué sirven
"""La base de html es que nos imaginamos que la página es un lienzo en blanco, y html se basa en etiquetas y se estructura pensando que ese canvas (lienzo, dom), html tiene cosas que lo puede estructurar en cositas, en pasos.
Si bien está en blanco hay cosas de dominio público(que lo ve todo el mundo) y están los metadatos(datos ocultos que le sirven al servidor para renderizar o mostrar datos en particular). Toda esta información está en el código html.
html tiene:
Cuerpo: <body> </body> la interfaz con los demás, lo que le voy a mostrar a otros, las cajitas, botoncitos. Es una etiqueta de apertura y cierre
<body>
        <form action = "http://localhost:5000/prendas/new/" method = "post">
            <h1>Agregá tu prenda</h1>
            <input name="name" placeholder="tipo de prenda">
        </form>  
   </body>
Cabeza: <head> </head> lo que no se le muestra al usuario, son todos los metadatos que le sirven al navegador para interpretar esa página

<h_> </h>→ los títulos, van del 1 a 6 (menor tamaño a mayor tamaño)
h1 → título más grande
"""
#🧗🏻‍♀️ Desafio IV: Buscá qué otras etiquetas semánticas y no semánticas existen
"""etiquetas semánticas: su nombre está relacionado con el código, leo el nombre y se que es. Se usan más porque son 
más entendibles y son más inclusivos."""


#----CIENCIA DE DATOS----
"""
personas = pd.read_csv("https://datasets.datos.mincyt.gob.ar/dataset/06ae9728-c376-47bd-9c41-fbdca68707c6/resource/11dca5bb-9a5f-4da5-b040-28957126be18/download/personas_2011.csv", sep=";")
personas.head()
"""
"""
sep → ver si está separado por comas o no

No son lo mismo:
NaN → no tiene datos, dato faltante, existe el objeto pero no tiene un dato asignado. Hay que ver qué hacer con esos faltantes, que paso. Como lo resuelvo
None, Null → no existe dato

Estudiar los datos: inspeccionar estadísticamente
Los datos son una representación numérica o categórica (es no numérico, o continuo) de mi sistema, o de los elementos de mi sistema. 
Busco patrones.
Hago estadística → todo lo que hacemos con los datos tiene un sustento estadístico

Método describe: te da una descripción general de los datos. Te dice cómo se distribuyen los datos, que patrones tengo. Con el describe tengo una intuición del tipo de distribución (como se comportan mis datos), que tengo.

Hay que tener cuidado con asumir que tiene distribución normal o no.
Histograma → solo para datos continuos, grafica la frecuencia de aparición de cada dato en el dataset.

Aplicación web para mostrar el análisis de los datos
"""

#-----7/11 Clase 16: limpieza de datos