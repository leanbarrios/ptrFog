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
