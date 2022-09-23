from turtle import title
from urllib import response
from mimetypes import init
import psycopg2
import requests
import time
import threading
import concurrent.futures

try:
    conn = psycopg2.connect(host="localhost", database="Concurrente", user="postgres", password="trolaso1928")
    cur = conn.cursor()
    print("Conexión exitosa")
except Exception as err:
    print('Error al conectar la base de datos')


def service(url):
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(get_service,url)

def get_service(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        photos = data
        for photo in photos:
            write_db(photo["title"])
    

def connect_db():
    pass

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


if __name__ == "__main__":
    url_site = ["https://jsonplaceholder.typicode.com/photos"]
    init_time = time.time()
    service(url_site)
    end_time = time.time() - init_time
    print(end_time)
    close_db()