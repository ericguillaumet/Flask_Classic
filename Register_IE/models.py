import sqlite3
from config import *
from Register_IE.connection import Connection

def select_all():

    connect = Connection("SELECT id,date,concept,quantity FROM movements order by date;")

    rows = connect.res.fetchall() #capturo las filas de datos
    columns = connect.res.description #capturo los nombres de columnas
    
    result = [] #lista para guardar diccionario

    for row in rows:
        data = {} #diccionario para cada registro
        position = 0

        for field in columns:
            data[field[0]] = row[position]
            position += 1
        result.append(data)

    connect.con.close()
    return result

def insert (register):
    connectInsert = Connection("insert into movements(date,concept,quantity) values(?,?,?)", register)
    connectInsert.con.commit() #Función que hace el registro
    connectInsert.con.close() #Cerrar conexión

def select_by(id):
    connectSelectBy = Connection(f"SELECT id,date,concept,quantity FROM movements WHERE id={id}")
    
    result = connectSelectBy.res.fetchall()
    connectSelectBy.con.close()

    return result[0]

def delete_by(id):
    connectDeleteBy = Connection(f"DELETE FROM movements WHERE id={id}")

    connectDeleteBy.con.commit()

    connectDeleteBy.con.close()

def update_by(id, register):
    connectUpdate = Connection(f"UPDATE movements SET date=?, concept=?, quantity=? WHERE id={id}", register)
    connectUpdate.con.commit()
    connectUpdate.con.close()