#-- @Autor: Maximiliano Rodrigo Soria
#-- Version: 1.0
#-- Python 2.7.13 
#-- Anio 2013
#-- Programacion en Tiempo real

import threading

def trabajo():
    """funcion que realiza el trabajo en el thread"""
    print 'Este es un hilo - Tomas se la come'
    return
threads = list()
for i in range(3):
    t = threading.Thread(target=trabajo)
    threads.append(t)
    t.start()
