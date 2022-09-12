#Expresiones regulares:

#Para pensar 🤔: ¿Qué usos crees que podemos darle a las expresiones regulares? Proponé una aplicación 
# concreta para tu carrera/disciplina.

#🧗‍♀️ Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?
"""
\d{4,}
"""

#🧗‍♀️ Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?
"""
[a-z]{3,6}
"""

#🧗‍♀️ Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?
"""
ab*
"""

#🧗‍♀️Desafio IV: ¿Qué expresión regular usarías para extraer el número de estudiantes que hay en una 
# clase según el siguiente texto: texto = 'En la clase de Introducción a la programación hay 30 estudiantes' 

"""
/d+
"""

#Desafio V: imprimí el fragmento del texto entre la posición 22 y 26 ¿Qué resultado obtenés? 
#¿Qué quiere decir el mensaje span?
import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."

patron = "amet"

resultado = re.search(patron,texto)


print(texto[22:26])

#Para pensar 🤔: ¿Qué resultado obtenemos con search()?¿Qué diferencias observan con match()?
# Ahora vamos a usar match. Este busca solo en el principio del string
"""
import re
texto = "lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet ."
patron = "lorem"
##Así puedo imprimir la busqueda
print(re.match(patron, texto).group())
"""

#Para pensar 🤔: ¿Qué resultado obtenemos? ¿Para qué sirve la función group()?
# Aca me argupa los valores que etsoy buscando
print("Este es el resultado de aplicar el group",resultado.group())




