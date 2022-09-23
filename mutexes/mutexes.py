import threading


videos=[
    'https://www.youtube.com/watch?v=E-DDmIhL4IM',
    'https://www.youtube.com/watch?v=2iVf6CtcasQ',
    'https://www.youtube.com/watch?v=bo9Z_pgByQY',
    'https://www.youtube.com/watch?v=xmPtVflvLh0',
    'https://www.youtube.com/watch?v=Vspk8Zz-xYk',
]


mutex = threading.Lock()
def crito(id):
    global x;
    x = x+ id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1

class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

    def run(self):
        mutex.acquire()
        crito(self.id)
        #print("valor" + str(self.id))
        mutex.release

hilos = [Hilo(1), Hilo(2), Hilo(3)]
x = 1
for h in hilos:
    h.start()