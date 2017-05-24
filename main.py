#-- @Autor: Maximiliano Rodrigo Soria
#-- Version: 1.0
#-- Python 2.7.13 
#-- Anio 2013
#-- Programacion en Tiempo real

from autos import *
from semaforo import *
from error import *
from punto_de_captura import *
from punto_visto import *
from conexion_hilos import *
from interfaz_grafica import *


#Esta clase crea una ventana 
class VentanaMonitor(Ventana):
	def __init__(self):		
		Ventana.__init__(self,"600","800","Monitor de objetos")
	
	def elementos(self,ventana):
		etiqueta = Label(ventana,text="Maxi prueba")
		etiqueta.pack()
	

def main():
	v=VentanaMonitor()
	v.iniciar() 
	

main()
