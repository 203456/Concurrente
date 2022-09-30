
import threading
import time
from unittest import result


mutex = threading.Lock()

def comer(Person):
    print("------------------------------------------------")
    print("                    A comer                     ")
    print("------------------------------------------------")
    Person.palillo=2
    hambre=True
    print("Persona = " +str(Person.id)+  " palillos: " +str(Person.palillo)+  " Hambre: " +str(hambre))
    print("Persona " +str(Person.id)+ " está comiendo")
    time.sleep(5)
    print("Ya está bien comido")
    Person.palillo=1
    hambre=False 
    print("Persona = " +str(Person.id)+  " palillos: " +str(Person.palillo)+  " Hambre: " +str(hambre))
    print("Siguiente persona")





class Persona(threading.Thread):
     def __init__(self, id, palillo):
        threading.Thread.__init__(self)
        self.id=id
        self.palillo=palillo

     def run(self):
        mutex.acquire()
        comer(self)
        mutex.release() 




    
if __name__ == "__main__":

    persona = [Persona(1,1), Persona(2,1), Persona(3,1), Persona(4,1), Persona(5,1), Persona(6,1), Persona(7,1), Persona(8,1)]
    for Person in persona:
        Person.start()


