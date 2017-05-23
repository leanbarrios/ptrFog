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
