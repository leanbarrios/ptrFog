from Tkinter import *
from ttk import *
import sys
#-- @Autor: Maximiliano Rodrigo Soria
#-- Version: 1.0
#-- Python 2.7.13 
#-- Anio 2013
#-- Programacion en Tiempo real

class Ventana():
	def __init__(self,alto,ancho,titulo):
		self._alto=alto
		self._ancho=ancho
		self._titulo=titulo
		
		
		
	def iniciar(self):
		ventana = Tk()	
		ventana.geometry(self._ancho+"x"+self._alto)
		ventana.title(self._titulo)
		self.elementos(ventana)
		
		
		ventana.mainloop()
		
	def elementos(self,ventana):
		pass

print("sadsdaa")
#titulo="Monitor de objetos"
#alto="600"
#ancho="800"
#v = Ventana(alto,ancho,titulo)
#v.iniciar()
