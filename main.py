#-- @Autor: Maximiliano Rodrigo Soria
#-- Version: 1.0
#-- Python 2.7.13 
#-- Anio 2013
#-- Programacion en Tiempo real

from auto_generico import *
from auto_patrullero import *
from semaforo import *
from error import *
from punto_de_captura import *
from punto_visto import *
#from conexion_hilos import *
from interfaz_grafica import *
from grafosConPesos import *


#Esta clase crea una ventana 
class VentanaMonitor(Ventana):
	def __init__(self):		
		Ventana.__init__(self,"600","800","Monitor de objetos")
	
	def elementos(self,ventana):
		etiqueta01 = Label(ventana,text="Objeto 1: ").grid(row=0,column=0)
		etiqueta02 = Label(ventana,text="Objeto 2: ").grid(row=1,column=0)
		etiqueta03 = Label(ventana,text="Objeto 3: ").grid(row=2,column=0)
		etiqueta04 = Label(ventana,text="Objeto 4: ").grid(row=3,column=0)
		etiqueta01 = Label(ventana,text="Auto policial: ").grid(row=0,column=1)
		etiqueta02 = Label(ventana,text="Auto generico: ").grid(row=1,column=1)
		etiqueta03 = Label(ventana,text="Error: ").grid(row=2,column=1)
		etiqueta04 = Label(ventana,text="Semaforo: ").grid(row=3,column=1)
	

def main():
	v=VentanaMonitor()
	v.iniciar() 
	

main()
