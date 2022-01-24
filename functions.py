import mysql.connector
from mysql.connector import errorcode
import config_database

####BackEnd Bot (Las siguientes funciones irian guardadas en otro archivo)

def connect(direccionip, usuario, contraseña, database):
    if contraseña == None:
        contraseña = ""

    try:
        mydb = mysql.connector.connect(
            host=f"{direccionip}",
            user=f"{usuario}",
            password=f"{contraseña}",
            database=f"{database}"
        )
        print(mydb)

        cur = mydb.cursor()
        cur.execute("SELECT VERSION()")
        data = cur.fetchone()
        print(f"Version: {data}")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Datos incorrectos usuario y/o contraseña")
            return False
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
            return False
        else:
            print(err)
            return False
    else:
        return True



##función borrador
def deluser(table, column, userd, ip, user, password, database):
    if password == None:
        password = ""
    mydb = mysql.connector.connect(
        host=f"{ip}",
        user=f"{user}",
        password=f"{password}",
        database=f"{database}"
    )
    cur = mydb.cursor()
    print("sensor A")
    for ii in range(len(column)):
        print(table[ii])
        print(column[ii])
        sql = f"DELETE FROM {table[ii]} WHERE {column[ii]} = '{userd}'"
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "record(s) deleted")

##Función recuperación datos guardados
def savedatas():
    creds = config_database.dats
    if len(creds) <= 0:
        return False
    else:
        return creds