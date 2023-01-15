import sqlite3
from config import *

def select_all():
    con = sqlite3.connect(ORIGIN_DATA) #Connection, check python SQL library
    cur = con.cursor()

    res = cur.execute("SELECT id,date,concept,quantity FROM movements order by date;")

    rows = res.fetchall() #capturo las filas de datos
    columns = res.description #capturo los nombres de columnas
    
    result = [] #lista para guardar diccionario

    for row in rows:
        data = {} #diccionario para cada registro
        position = 0

        for field in columns:
            data[field[0]] = row[position]
            position += 1
        result.append(data)

    con.close()
    return result

def insert (register):
    con = sqlite3.connect(ORIGIN_DATA) #Connection, check python SQL library
    cur = con.cursor()
    cur.execute("insert into movements(date,concept,quantity) values(?,?,?)", register)

    con.commit() #Función que hace el registro

    con.close()