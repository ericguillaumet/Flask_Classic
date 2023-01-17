import sqlite3
from config import *
from Register_IE.connection import Connection

def select_all():

    con = Connection("SELECT id,date,concept,quantity FROM movements order by date;")

    rows = con.res.fetchall() #capturo las filas de datos
    columns = con.res.description #capturo los nombres de columnas
    
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
    con = Connection("insert into movements(date,concept,quantity) values(?,?,?)", register)

    con.commit() #Función que hace el registro

    con.close() #Cerrar conexión

def select_by(id):
    con = Connection(f"SELECT id,date,concept,quantity FROM movements WHERE id={id}")
    
    result = con.res.fetchall()
    return result[0]

def delete_by(id):
    con = Connection(f"DELETE FROM movements WHERE id={id}")

    con.commit()

    con.close()