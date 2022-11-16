# Clase practica 16/09
#POO

#Ejercicio 1:
#Dada la siguiente clase, identificá la interfaz y el estado de la misma:
"""
El nombre de la clase: Pero
La interfaz: el conjunto de mensajes que entiende (metodos), los metodos, sin el init que es el contructor
El estado: el conjunto de atributos-->
        self._alimento = 0
        self._caricias = 0
"""

"""
class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

"""

#Ejercicio 2
#Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda volar 
#si al hacerlo la energía toma el valor 0 o valor negativo.


def volar(self, kms):
    if (10 + kms <= self.energia):
        self.energia -= 10 + kms
    else:
        print("No puede volar esa distancia, no tiene suficiente energia")

#con el if si la condicion no se cumple la condicion se ejecuta igual con el try o raise se frena el codigo

#Ejercicio 3
#Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un 
#descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que 
#devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase 
#y en algunos casos aplicar este descuento.

class Notebook:
    def __init__(self, marca, modelo, precio): #los atributos van a tener un valor incial que yo no le tengo que pasar como atributo
        self.marca = marca #self.marca es el atributo que es distinto del parametro marca
        self.modelo = modelo
        self.precio = precio

#si no se sabe le valor lo paso como parametro, sino solo como atributo
# el estado son los atributos, self.algo
#los parametros son los que aparecen entre parentesis

    def descuento(self, porcentaje):
        self.precio = self.precio - (self.precio * (porcentaje/100))

#getter devuelve le valor del atributo en ese momento
    def precioactual(self): #estamos llamando a una metodo y no a un atributo
        return self.precio

# Hay que instanciar y hacer un ejemplo: diferencia entre definir una clase e instanciar un objeto
#El objeto se crea recien cuando lo instanciasmo

notebook1 = Notebook("sus", "R556L", 80000)
notebook1.descuento(50)
print(notebook1.precioactual())

#para ejecutar un metodo aunque no tenga parametrros tiene que tener parentesis sino no funciona


#Ejercicio 4
# Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, 
# recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible 
#indicar directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:

#getter es un metodo para obetener el valor y un setter es para modeificar el valor, lo setea

class Contador:
    def __init__(self,valor):
        self.valor = valor #es un parametro el valor pq no tiene valor inicial 0

    def inc(self):
        self.valor += 1

    def dis(self):
        self.valor -= 1
    
    def reset(self):
        self.valor = 0

    def valorActual(self): #seria el getter
        print(self.valor)

    def valorNuevo(self, nuevoValor): #como argumento le paso un valor y se lo asigna al Atributo, es el setter
        self.valor = nuevoValor

#Ejercicio 5
#Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, 
# en forma de mensaje. Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" (para 
# cuando se coloca un valor nuevo). El método para saber el último comando es ultimoComando, y el resultado de 
# aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución"

class Contador:
    def __init__(self,valor):
        self.valor = valor #es un parametro el valor pq no tiene valor inicial 0
        self.comando = None

    def inc(self):
        self.valor += 1
        self.comando = "Incrementar"

    def dis(self):
        self.valor -= 1
        self.comando = "Disminuir"

    def reset(self):
        self.valor = 0
        self.comando = "Resetear"

    def valorActual(self): #seria el getter
        print(self.valor)

    def valorNuevo(self, nuevoValor): #como argumento le paso un valor y se lo asigna al Atributo, es el setter
        self.valor = nuevoValor

    def utlimoComando(self):
        print(self.comando)


#Ejercicio 6
#Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. Este objeto 
#debe entender los siguientes mensajes:

#necesitas tener la misma cantidad de getters que la cantidad de atributos

#el setter es un metodo que asigna un valor a ese atributo y por eso no tenes que tener si o si 
#la misma cnatidad de setter que de atributos

class Claculadora:
    def __init__(self):
        self.valor = None #lo inicializo vacio porque despues lo crago

    def cargar(self, valor): #defino el metodo cragar que le de valor al atributo --> es un setter
        self.valor = valor

    def sumar(self,numero):
        self.valor += numero

    def restar(self,numero):
        self.valor -= numero

    def multiplicar(self,numero):
        self.valor *= numero

    def valorActual(self):
        print(self.valor)

#Ejercicio 7:

class Gorriones:
    def __init__(self): #no te dan los atributos vos lo tenes que deducir
        self.gramosActuales = 0
        self.kmsActuales = 0 
        self.listaGramos = []
        self.listaKms = [] #lo guardamos para saber cuantas veces volo

    def comar(self, gramos):
        self.listaGramos.append(gramos)
        self.gramosActuales += gramos

    def volar(self, kms):
        self.listaKms.append(kms)
        self.kmsActuales += kms

    def css(self):
        if self.gramosActuales > 0:
            return self.kmsActuales / self.gramosActuales
        else:
            return None
#las listas pueden variar en longitud, y atributos

    def cssp(self):
        return max(self.listaKms) / max(self.listaGramos)

    def cssv(self):
        return len(self.listaKms) / len(self.listaGramos)

    def estaEnEquilibrio(self):
        return 0,5 <= self.css <= 2


#-----------------------------------------------------------------
#PARTE 2:

#Ejercicio 1:

# atributos: alimenot y caricias
#metodos: energia, comer,
#interfaz: lista de metodos, mensjaes que entiende, no lo que hace

#si comparte parte de la interfaz (caricias), no comparten toda.
#para que sean polimorficas, dependa de que una tercer clase puede usar indistintamente a estas dos clases. por ejemplo humano
#le dice comer a perro y gato, los dos entienden (son polimorficos), pero no queiere decir que hagan lo mismo.
#solo sabe mandarle el mensaje, peor no puede ver el efecto del mensaje
 
#Polimorficas: dos clases que comparten al menos parte de su interfaz y que pueden recibir un mensaje de una tercera/ser 
#usadas por una tercera
"""class Perro:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):
        self.alimento += gramos

    def alimento(self):
	print(self.alimento)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 2

    def pasear(self, km):
	self.alimento -= km / 4

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

    def caricias(self):
	print(self.caricias)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 4"""

#Ejercicio 2:

class Golondrina:
    def __init__(self, energia):
        self.energia = energia

    def comer_alpiste(self, gramos):
        self.energia += 4 * gramos

    def volar_en_circulos(self):
        self.volar(0)

    def volar(self, kms):
        self.energia -= 10 + kms

    def esta_debil(self):
        return self.energia < 10

    def esta_feliz(self):
        return self.energia >= 500

    def esta_en_equilibrio(self):
        150<= self.energia <= 300

#Ejercicio 3:

class Ornitologo:
    def __init__(self): #solo interactua con aves, por eso su atributo es las aves con las q interactua
        self.aves = []

    def estudiarAves(self, ave):
        self.aves.append(ave)

    def avesEnEstudio(self): #es un getter
        return self.aves

    def avesEnEquilibrio(self):
        return [self.aves[i].estaEnEquilibrio() for i in range(len(self.aves))]

    def realizarRutina(self):
        [self.aves[i].comer(80) for i in range(len(self.aves))]

ornitologo1 = Ornitologo()


#Ejercicio 4:
class MedioDeTransporte:
    def __init__(self, combustible):
        self.combustible = combustible

    def combustibleActual(self):
        return self.combustible

    def entran(self,personas):
        return personas <= self.maximoPersonas()

class Moto(MedioDeTransporte):
    def maxPeronas(self):
        return 2
    
    def recorrer(self, km):
        self.combustible -= km 

class Auto(MedioDeTransporte):
    def maxPeronas(self):
        return 5
    
    def recorrer(self, km):
        self.combustible -= km/2

#Ejemplo Parcial:
"""En un mundo distópico la humanidad es atacada sin descanso por titanes. Estos titanes son muy resistentes pero 
no inmortales, su salud (100 de máxima) puede ir disminuyendo si reciben daño debido a algún ataque, y si llega a 0 
se muere. Al recibir este ataque la salud disminuye 1.5 por cada puntos de daño recibido. Además tienen la capacidad 
de destruir cierto número de casas dependiendo de su salud, siendo 8 casas cuando su salud es máxima o un número 
proporcional si su salud es menor a la máxima (si tiene 60 puntos de salud destruiría 4.8 casas, es decir, 4 casas 
completas y más de la mitad de otra). Sin embargo no tienen la capacidad de comunicarse con los humanos, siendo un 
grito, "¡Aaaarrrg!", el único sonido que hacen. Definí la clase Titan con los atributos y métodos correspondientes. 
Además instanciá a un Titan y ejecutá las siguientes líneas:
"""
#------------------------------------------------------
class Titan:
    def __init__(self, salud):
        self.salud = salud
    
    def recibir_ataque(self, danio):
        self.salud -= danio * 1.5

    def esta_vivo(self):
        if self.salud > 0:
            return True
        else:
            "El titan ha fallecido" 

    def salud_actual(self): #el getter
        return self.salud

    def cuantas_casas(self):
        return (self.salud * 8/100) 

    def grito(self):
        return "¡Aaaarrrg!"

    def destruir_casas(self):
        if (self.cuantas_casas() > 1):
            if ((self.cuantas_casas() % 1)) > 0: # quiere decir que la division no da entera ## el % devuelve el resto de la division
                self.salud -= (self.cuantas_casas() // 1 ) * (100/8) # el // devuelve la parte entera de la division
            else:
                self.salud -= (self.cuantas_casas() - 1) * (100/8)
        else: 
            print("No puede destruir ninguna casa")

#------Ejercicio ENTERPRISE:
class Enterprise:
    def __init__(self):
        self.coraza = 5
        self.potencia = 50

    def potencia_actual(self):
        return self.potencia
    
    def coraza_actual(self):
        return self.coraza

    def encontrarPilaAtomica(self):
        if self.potencia + 25 <= 100:
            self.potencia += 25
        else:
            self.potenica = 100

    def encontrarEscudo(self):
        if self.coraza + 10 <= 20:
            self.coraza += 10
        else:
            self.coraza = 20

    def recibirAtaque(self, puntos):
        if puntos <= self.coraza:
            self.coraza -= puntos
        else:
            self.potencia -= (puntos - self.coraza)
            self.coraza = 0

    def fortalezaDefensiva(self):
        return (self.coraza + self.potencia)

    def necesitaFortalecerse(self):
        if self.coraza == 0 and self.potencia < 20:
            return True

    def fortalezaOfensiva(self):
        if self.potencia >= 20:
            return ((self.potencia - 20)/2)
        else:
            return 0

#-----------------Ejercicio ESTUDIANTES
class Persona:
    def __init__(self, energia):
        self.energia = energia 

    def energia_actual(self): #getter
        return self.energia
    
    def dormir(self, horas):
        if self.energia + horas * 100/8 <= 100:
            self.energia += horas * 100/8
        else:
            self.energia = 100

    def comer(self):
        if self.energia + 10 <= 100:
            self.energia += 10
        else:
            self.energia = 100

    def hacer_ejercicio(self, minutos):
       self.energia -= 25 * minutos/30

    def estado_animo(self):
        return "No esta Feliz"    

class Estudiante(Persona): 
    def estudiar(self, cantidad_horas):
        self.energia -= 20 * cantidad_horas

    def aporbar(self):
        self.estado_animo = "Feliz"
        return True
        
estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())
    

#---------------PRACTICA DE NUEVO
#Ejercicio 3
#Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un 
#descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que 
#devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase 
#y en algunos casos aplicar este descuento.


class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento(self, procentaje):
        self.precio = self.precio * (self.precio * procentaje/100)

notebook1 = Notebook("Mac", "Serie 5", "1590")
notebook1.descuento(30)

#Ejercicio 4
# Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, 
# recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible 
#indicar directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:

class Contador:
    def __(self, valor):
        self.valor = valor
        self.comando = None

    def inc(self):
        self.valor += 1
        self.comando = "Aumentar"

    def dis(self):
        self.valor -= 1
        self.comando = "Disminuir"

    def reset(self):
        self.valor += 0
        self.comando = "Resetear"


    def valor_actual(self):
        return self.valor 
        
    def valor_nuevo(self, nuevo_valor):
        self.valor = nuevo_valor

    def ultimo_Comando(self):
        print(self.comando)
       
#Ejercicio 5
#Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, 
# en forma de mensaje. Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" (para 
# cuando se coloca un valor nuevo). El método para saber el último comando es ultimoComando, y el resultado de 
# aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución"

class Calculadora:
    def __init__(self):
        self.valor = None

    def cargar_numero(self, numero):
        self.valor = numero

    def sumar(self, numero):
        self.valor += numero
    
    def restar(self, numero):
        self.valor -= numero
    
    def multiplicar(self, numero):
        self.valor *= numero

    def valor_actual(self):
        print(self.valor)

#Ejercicio 7:

class Gorriones:
    def __init__(self):
        self.totalkms = []
        self.totalcomida = []
        self.kms = None
        self.comida = None

    def comer(self, gramos):
        self.totalcomida.append(gramos)
        self.comida += gramos

    def volar(self, kms):
        self.totalkms.append(kms)
        self.kms += kms
    
    def css(self):
        if self.comida > 0:
            self.kms / self.comida
        else:
            return None

    def cssp(self):
        return max(self.totalkms)/max(self.totalcomida)

    def cssv(self):
        return len(self.totalkms)/len(self.totalcomida)

    def esta_en_equilibrio(self):
        return 0.5 <= self.css <= 2

#---------------------------EXTRAS
##A continuación creamos la clase `Persona`. Una persona tendrá un DNI, un #nombre y una edad.
#
#* Creamos el constructor.
#* Crearemos también los métodos seters y getters.
#* Se debe definir el método `mostrar()` para imprimir los datos de la persona.
##Vamos a realizar la clase `DNI` donde vamos a guardar el número de DNI (lo #vamos a guardar en una cadena de longitud 8) y la letra correspondiente.
#
#* Vamos a crear el constructor, que recibe el número de DNI y calcula #automáticamente la letra.
#* Crearemos también los métodos seters y getters.
#* Se debe definir el método `mostrar()` para imprimir el DNI.
class Persona:
    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
    
    def get_dni(self):
        return self.dni 
    def get_nombre(self):
        return self.nombre
    def edad_actual(self):
        return self.edad
    
    def nombrar(self, nombre):
        self.nombre = nombre

    def validar_dni(self):
        if len(self.dni) != 9:
            print("DNI incorrecto!")
            self.dni = ""
        
    def dni(self, id):
        self.dni = id
        self.validar_dni()

    def edad(self, edad):
        if edad < 0:
            print("Edad incorrecta")
            self.edad = 0 
        else:
            self.edad = edad

    def mostrar(self):
        return "Nombre: "+self.nombre, "Dni: "+self.dni, "Edad: "+self.edad








