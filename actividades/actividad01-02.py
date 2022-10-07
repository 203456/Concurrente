import threading
import time
from threading import Semaphore
semaforo = Semaphore(1)
stop = Semaphore(1)

CONSUMIDORES = 8
PRODUCTORES = 6
CONTADOR = 10
BODEGA = []

class Productor(threading.Thread):
    items = 1
    conta = 0

    def __init__(self,):
        super(Productor, self).__init__()
        self.id = Productor.conta
        Productor.item = 1
        Productor.conta += 1

    def Producir(self):
        if len(BODEGA) > 9:
            print('La bodega esta llena')
            stop.acquire()
            print(BODEGA)

        else:
            stop.release()
            print('El productor ' +str(self.id)+ ' esta agregando un item')
            BODEGA.append(Productor.items) 
            time.sleep(5)
            print('estado de la bodega ' +str(len(BODEGA)))

    
    def run(self):
        for i in range(CONTADOR):
            time.sleep(0.15)
            semaforo.acquire()
            self.Producir()
            semaforo.release()
 


class Consumidor(threading.Thread):
    items = 1
    conta = 0

    def __init__(self,):
        super(Consumidor, self).__init__()
        self.id = Consumidor.conta
        Consumidor.item = 1
        Consumidor.conta += 1
    
 

    def Consumir(self):
        if len(BODEGA) < 1:
            print('La bodega esta vacia')
            stop.acquire()

        else:
            stop.release()
            print('El consumidor ' +str(self.id)+ ' esta consumiendo un item')
            BODEGA.remove(Consumidor.items)
            time.sleep(5)
            print('Estado de la bodega: '+str(len(BODEGA)))

    def run(self):
        for i in range(CONTADOR):
            time.sleep(0.15)
            semaforo.acquire()
            self.Consumir()
            semaforo.release()
  



def main():
    productores = []
    consumidores = []

    for i in range(PRODUCTORES):
        productores.append(Productor())

    for p in productores:
        p.start()


    for i in range(CONSUMIDORES):
        consumidores.append(Consumidor())
        
    for c in consumidores:
        c.start()




if __name__ == '__main__':
    main()
