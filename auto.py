#-- @Autor: Maximiliano Rodrigo Soria
#-- Version: 1.0
#-- Python 2.7.13 
#-- Anio 2013
#-- Programacion en Tiempo real

class Auto():
	def __init__(self, modelo,tipo, patente):
		self._modelo = modelo
		self._tipo = tipo
		self._velocidad = 0
		self._estado =  ""
		self._patente = patente
		
	def setEstado(self, estado):
		self._estado=estado	
	
	def getEstado(self):
		return self._estado
		
	def arrancar(self):
		pass
	
	def frenar(self):
		pass
	
	def devolverModelo(self):
		return self._modelo	
	
