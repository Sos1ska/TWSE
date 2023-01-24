import sqlite3
from .important_func import path_os

def _insert(way, table, *info):
    data_local=info
    try : connect_db=sqlite3.connect(path_os(way))
    except sqlite3.DatabaseError : print(f'[ record_database ] - [ Not found DataBase -> {path_os(way)} ]')
    cur=connect_db.cursor()
    match table:
        case "IP":
            cur.execute("""INSERT INTO IP VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", data_local)
            connect_db.commit()
        case "Number":
            cur.execute("""INSERT INTO Number_phone VALUES(?, ?, ?, ?, ?, ?)""", data_local)
            connect_db.commit()
        case "MAC":
            cur.execute("""INSERT INTO MAC VALUES(?, ?, ?)""", data_local)
            connect_db.commit()
