#-- @Autor: Maximiliano Rodrigo Soria
#-- Version: 1.0
#-- Python 2.7.13 
#-- Anio 2013
#-- Programacion en Tiempo real

class PuntoVisto():
	def __init__(self, estado):		
		self._estado =  ""
		
	def setEstado(self, estado):
		self._estado=estado	
	
	def getEstado(self):
		return self._estado



def punto_visto():
	print("Soy un punto visto")


punto_visto()
