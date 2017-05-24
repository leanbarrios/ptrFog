from Tkinter import *
from ttk import *
import sys

class Ventana():
	def __init__(self,alto,ancho,titulo):
		self._alto=alto
		self._ancho=ancho
		self._titulo=titulo
		
		
	def iniciar(self):
		ventana = Tk()	
		ventana.geometry(self._ancho+"x"+self._alto)
		ventana.title(self._titulo)
		etiqueta = Label(ventana,text="Maxi prueba")
		etiqueta.pack()
		ventana.mainloop()

print("sadsdaa")
#titulo="Monitor de objetos"
#alto="600"
#ancho="800"
#v = Ventana(alto,ancho,titulo)
#v.iniciar()
