#SEGUNDO PARCIAL

#------CLASE 11: INTRODUCCION A WEB-----

""""arquitectura cleinte-servidor

protocolo HTTP --> comunicacion entre cliente y servidor"""

#🤔 Para pensar: ¿qué tecnologías se usan en la Web? ¿En qué se desarrolla un cliente? ¿Y un servidor?

#Softwares y tecnologías de un lado y el otro:
#- Servidor: python, note, ruby, java, las base de datos(sql), se espera que ejecute, procese y almacene.
#- Cliente: javascript, ccs, html, se renderizan los recursos en el navegador(software), dialoga el navegador.

"""
HTTP es un protocolo que tiene ciertas características:
Ante cada pedido de un cliente el servidor envía una respuesta, no da respuestas si el cliente no pidió nada.
No maneja ningún concepto de memoria de pedidos anteriores, “ me pido esto antes..”
Lo que se intercambia en general es texto, aun cuando estés mandado otro recursos como una página web, el protocolo solo envia texto
Está basado en códigos de respuesta, como etiquetas, que te dan idea de si funciona la comunicación o no.


Para poder hacer esa renderización de los datos voy a usar algunas tecnologías como 
- html: es un lenguaje, aunque no opera contra el sistema operativo, basado en etiquetas, texto que dado algunos caracteres que tienen cierto significado me va a estructurar el texto de forma tal que yo pueda visualizar en la pantalla con esa estructura.
- ccs: lenguaje que permite poner las cosas bonitas, como el maquillaje, en base a lo que te pasa html.
- javascript: es un lenguaje de programación que te permite hacer o dinamizar las estructuras que definimos o maquillamos con las anteriores, cosas más complejas.

"""


