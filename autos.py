class Auto():
	def __init__(self, modelo,tipo):
		self._modelo = modelo
		self._tipo = tipo
		self._velocidad = 0
		
class Patrullero(Auto):
	    def __init__(self):
			pass

class Auto_Generico(Auto):
	    def __init__(self):
			pass


def auto_prueba():
	print("Tengo mi auto generico y el patrullero")


auto_prueba()
