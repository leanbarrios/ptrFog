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
