class Auto():
	def __init__(self, modelo,tipo):
		self._modelo = modelo
		self._tipo = tipo
		self._velocidad = 0
		self._estado =  ""
		
	def setEstado(self, estado):
		self._estado=estado	
	
	def getEstado(self):
		return self._estado

		
class Patrullero(Auto):
	    def __init__(self):
			pass

class Auto_Generico(Auto):
	    def __init__(self):
			pass


def auto_prueba():
	print("Tengo mi auto generico y el patrullero")


auto_prueba()
