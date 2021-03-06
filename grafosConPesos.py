from collections import deque
from auto import *
class Grafo(object):
    def __init__(self):
        self.relaciones = {}
    def __str__(self):
        return str(self.relaciones)

class Arista(object):
    def __init__(self, elemento, peso, lleno,delincuente):
        self.elemento = elemento
        self.peso = peso 
        self.lleno = 0
        self.delincuente=False
    def __str__(self):
        return str(self.elemento) + str(self.peso)

    def agregar_quitar_lleno(self, numero):
    	if (self.lleno-numero) < 0 and (self.lleno+numero) > 100:
    		
    	else:
    		self.lleno=self.lleno+numero
    def getLleno(self):
    	return lleno
    def setDelincuente(self):
    	if self.delincuente==False:
    		self.delincuente=True
    	elif self.delincuente==True:
    		self.delincuente=False
    def getDelincuente(self):
    	return self.delincuente	    

    	 
 
def agregar(grafo, elemento):
    grafo.relaciones.update({elemento:[]})

def relacionar(grafo, elemento1, elemento2, peso = 1):
    relacionarUnilateral(grafo, elemento1, elemento2, peso)
    relacionarUnilateral(grafo, elemento2, elemento1, peso)
    
def relacionarUnilateral(grafo, origen, destino, peso):
    grafo.relaciones[origen].append(Arista(destino, peso)) 
    

def caminoMinimo(grafo, origen, destino):
    etiquetas = {origen:(0,None)}
    dijkstra(grafo, destino, etiquetas, [])
    return construirCamino(etiquetas, origen, destino)

def construirCamino(etiquetas, origen, destino):
    if(origen == destino):
        return [origen]
    return construirCamino(etiquetas, origen, anterior(etiquetas[destino])) + [destino]
    
    
def dijkstra(grafo, destino, etiquetas, procesados):
    nodoActual = menorValorNoProcesado(etiquetas, procesados)
#    print "-----------------------------"
#    print "Nodo Actual:",nodoActual
#    print "Procesados",procesados
#    print "Etiquetas",etiquetas
    if(nodoActual == destino): 
        return
    procesados.append(nodoActual)
    for vecino in vecinoNoProcesado(grafo, nodoActual, procesados):
        generarEtiqueta(grafo, vecino, nodoActual, etiquetas)
    dijkstra(grafo, destino, etiquetas, procesados)

def generarEtiqueta(grafo, nodo, anterior, etiquetas):
    etiquetaNodoAnterior = etiquetas[anterior]
    etiquetaPropuesta = peso(grafo, anterior, nodo) + acumulado(etiquetaNodoAnterior),anterior
    if(not(etiquetas.has_key(nodo)) or  acumulado(etiquetaPropuesta) < acumulado(etiquetas[nodo]) ):
        etiquetas.update({nodo:etiquetaPropuesta})

def aristas(grafo, nodo):
    return grafo.relaciones[nodo]
        
def vecinoNoProcesado(grafo, nodo, procesados):
    aristasDeVecinosNoProcesados = filter(lambda x: not x in procesados, aristas(grafo,nodo))
    return [arista.elemento for arista in aristasDeVecinosNoProcesados]


def peso (grafo, nodoOrigen, nodoDestino): 
    return reduce(lambda x,y: x if x.elemento == nodoDestino else y, grafo.relaciones[nodoOrigen]).peso 

def acumulado(etiqueta):
    return etiqueta[0]

def anterior(etiqueta):
    return etiqueta[1]
           
def menorValorNoProcesado(etiquetas, procesados):
    etiquetadosSinProcesar = filter(lambda (nodo,_):not nodo in procesados, etiquetas.iteritems())
    return min(etiquetadosSinProcesar, key=lambda (_, (acum, __)): acum)[0]
  
    
    

grafo=Grafo()
def creador (grafo):
	cantidad=input("manzanas a crear en horizontal")
	cantidad2=input("manzanas a crear en vertical")
	total=cantidad1*(cantidad2+1)
	variable=0
	while total >variable:
		grafo.agregar(grafo,variable)
		variable=variable+1
	variable=0
	while variable<total:
		grafo.relacionar(grafo,variable,variable+1)
		grafo.relacionar(grafo,variable,variable+cantidad)
		grafo.relacionar(grafo,variable,variable+cantidad+1)
		variable=variable+1	
    
    
    


    
