from turtle import title
from urllib import response
from mimetypes import init
import psycopg2
import requests
import time
import threading
import concurrent.futures
import pytube

videos=[
    'https://www.youtube.com/watch?v=E-DDmIhL4IM',
    'https://www.youtube.com/watch?v=2iVf6CtcasQ',
    'https://www.youtube.com/watch?v=bo9Z_pgByQY',
    'https://www.youtube.com/watch?v=xmPtVflvLh0',
    'https://www.youtube.com/watch?v=Vspk8Zz-xYk',
]
try:
    conn = psycopg2.connect(host="localhost", database="Concurrente", user="postgres", password="trolaso1928")
    cur = conn.cursor()
    print("Conexión exitosa")
except Exception as err:
    print('Error al conectar la base de datos')

 
def download_videos():
    for x in range(0, 5):

        v1 = pytube.YouTube(videos[x])
        v1.streams.first().download()
        print("Video descargado")

def get_services(dato):
   response = requests.get('https://randomuser.me/api/')
   if response.status_code == 200:
       print(f'Dato = {dato}') 
       results = response.json().get('results')
       name = results[0].get('name').get('first')
       print(name)
 

def insercion():
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    if response.status_code == 200:
        data = response.json()
        photos = data
        for photo in photos:
            write_db(photo["title"])

def write_db(title):
    try:
        cur.execute("INSERT INTO datos (title) Values ('"+title+"')")
    except Exception as err:
        print('Error en la inserción: '+ err)
    else:
        conn.commit()
def close_db():
    try:
        cur.close()
        conn.close()
        print("Base de datos cerrada correctamente")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    thVideos = threading.Thread(target=download_videos)
    thInsercion = threading.Thread(target=insercion)
    thInsercion.start()
    thVideos.start()
    for x in range(0,50):
        th1 = threading.Thread(target=get_services, args=[x])
        th1.start()
        #get_services()
