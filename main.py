from autos import *
from semaforo import *
from error import *
from punto_de_captura import *
from punto_visto import *
from conexion_hilos import *
from interfaz_grafica import *

class VentanaMonitor(Ventana):
	def __init__(self):		
		Ventana.__init__(self,"600","800","Monitor de objetos")
	

def main():
	v=VentanaMonitor()
	v.iniciar() 
	

main()
