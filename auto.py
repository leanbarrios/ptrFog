#-- @Autor: Maximiliano Rodrigo Soria
#-- Version: 1.0
#-- Python 2.7.13 
#-- Anio 2013
#-- Programacion en Tiempo real
import random
from error import *

class Auto():
	def __init__(self, modelo, tipo, patente):
		self._modelo = modelo
		self._tipo = tipo
		self._velocidad = 0
		self._estado =  ""
		self._patente = patente
		
	def setEstado(self, estado):
		self._estado=estado	

	def getEstado(self):
		return self._estado

	def setVelocidad(self, velocidad):
		self._velocidad=velocidad

	def getVelocidad(self):
		return self._velocidad
		
	def arrancar(self):
		#pregunta si el auto ya esta en movimiento
		if self._velocidad != 0:
			return "Auto esta en movimiento!"
		#si el auto no esta en movimiento, pregunta si esta detenido
		elif self._velocidad == 0: 
			self._velocidad = 1
			return "Auto arranco"
		#si los 2 casos anteriores no se dieron, significa que falla cumplio con su objetivo (falta esa parte)
		else:
			return "Auto no arranco. Falla logro su objetivo"
	
	def frenar(self):
		#pregunta si el auto ya estaba detenido
		if self._velocidad == 0:
			return "Auto ya esta detenido!"
		#si el auto no esta detenido, pregunta si esta en movimiento
		elif self._velocidad != 0:
			self._velocidad = 0
			return "Auto se detuvo"
		##si los 2 casos anteriores no se dieron, significa que falla cumplio con su objetivo (falta esa parte)
		else:
			return "Auto no freno. Falla logro su objetivo"
	
	def devolverModelo(self):
		return self._modelo	
#Ejemplo
#auto = Auto("ford fiesta", "auto", "abc123")
#auto.setVelocidad(1)
#print auto.frenar()

