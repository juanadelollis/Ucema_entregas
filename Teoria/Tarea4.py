#Clase 09/09
#POO
#Introduccion a la POO

#DESAFIO
#Hacer esta_debil: si tienen menos de 10 puntos de energia (golondrinas) o 50 (dragones)
#Hacer esta_feliz: si tiene más de 500 puntos de eneria (sin importar cuál)

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def esta_debil(self):
    return self.energia < 10

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



