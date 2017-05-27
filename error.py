#-- @Autor: Maximiliano Rodrigo Soria
#-- Version: 1.0
#-- Python 2.7.13  mmm
#-- Anio 2013
#-- Programacion en Tiempo real

class Error():
	def __init__(self, estado):		
		self._estado =  ""
		
	def setEstado(self, estado):
		self._estado=estado	
	
	def getEstado(self):
		return self._estado
		
		
def error():
	print("Soy un error")


error()
