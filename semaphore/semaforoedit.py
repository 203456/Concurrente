from threading import Thread, Semaphore
from tkinter import Y
import pytube
semaforo = Semaphore(1) #Crea la variable semaforo


videos=[
    'https://www.youtube.com/watch?v=E-DDmIhL4IM',
    'https://www.youtube.com/watch?v=2iVf6CtcasQ',
    'https://www.youtube.com/watch?v=bo9Z_pgByQY',
    'https://www.youtube.com/watch?v=xmPtVflvLh0',
    'https://www.youtube.com/watch?v=Vspk8Zz-xYk',
]


def critico(id):
    for x in range(0, 5):

        v1 = pytube.YouTube(videos[x])
        v1.streams.first().download()
        print("Video descargado")


class Hilo(Thread):
    def __init__(self, id, videos):
        Thread.__init__(self)
        self.id=id
        self.videos=videos

    def run(self):
        semaforo.acquire() #Inicializa semafoeo, lo adquiere
        critico(self.id)
        semaforo.release() #Lubera un semaforo e incrementa la variable semaforo
        

threads_semaphore = [Hilo(1, videos[0]), Hilo(2, videos[1]), Hilo(3, videos[2]), Hilo(4, videos[3]), Hilo(5, videos[4])]
for t in threads_semaphore:
    t.start()