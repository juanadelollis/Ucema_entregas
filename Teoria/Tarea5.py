#Clase 09/09
#POO
#Introduccion a la POO

#DESAFIO
#Hacer esta_debil: si tienen menos de 10 puntos de energia (golondrinas) o 50 (dragones)
#Hacer esta_feliz: si tiene más de 500 puntos de eneria (sin importar cuál)
""""
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

class Dragon:     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def tomar_carrera(self): #la deifninmos en clase
    self.energia -= 2

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def esta_debil(self):
    return self.energia < 50

  def esta_feliz(self):
    return self.energia >= 500

pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)

"""
#Clase 16/09

#POO

#Como hay un metodo "esta_feliz" que hace lo mismo qen las dos clases, lo comparten completamente.
#Son polimorficos porque entienden los mismos mensajes pero hace cosas distintas

#Podemos ponerlo arriba en la clase mayor --> animales alados

class animales_alados:
  def esta_feliz(self):
    return self.energia >= 500

class Golondrina(animales_alados):
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

class Dragon(animales_alados):     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def tomar_carrera(self): #la deifninmos en clase
    self.energia -= 2

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def esta_debil(self):
    return self.energia < 50

  

pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)

#Definimos la clase madre, pero todavia las otras clases no saberm que son parte de esta por eso, 
# hay que decirle que hereda las caracteristicas de animal alado
""""
class animales_alados:
  def esta_feliz(self):
    return self.energia >= 500
"""

"""class Golondrina(animales_alados): y lo mismo con Dragon"""
#Heredar queiere decir que siguen entendiendo el mensaje 
#pero no porque lo tienen como emtodo proopio sino pq lo heredan como caracteristicas de otra clase

#Desafio:
#Hace a hipo, entrenador de dragones: sabe aceptar a dragones y luego hacerlos entrenar, haciendoles 
#dar 20 vueltas en circulos y luego comer su comida favorita hasta saciarse (3 peces)

#Vamosa definir una clase que es entrenadro de dragones
#si sabe aceptar es algo inherente a esa clase, lo inicializo con init

class EntrenadorDragones:
  def __init__(self, equipo):
    self.equipo = equipo #le decimos que es un atributo de estos objetos

#no entiende todavia el metodo de aceptar el dragon

  def aceptar_dragones(self, dragon): #tiene que ser una lista para que los pueda agrupar,preever que tipo de dato es
    self.equipo.append(dragon)

#ahora si acepta dragones

  def hacer_entrenar(self, dragon): #le pasamos el nombre del dragon que queremos entrenar
    for vueltas in range(20):
      dragon.volar_en_circulos()
    dragon.comer_peces(3) #le saco el tab porque estaba adentro del for, lo iba a ser 20 veces

  def entenar_equipo(self):
    for dragon in self.equipo:
      self.hacer_entrenar(dragon)

Hipo = EntrenadorDragones([roberta]) #ahi lo definimos, y lo instanciamos
