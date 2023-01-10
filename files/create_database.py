import sqlite3
try : from LOGer import autolog_color
except ImportError : from .core import autolog_color
from .important_func import path_os

def _create(way, way_error_log, way_general_log):
    connect=sqlite3.connect(path_os(way=way))
    cur=connect.cursor()
    try:
        cur.executescript("""
BEGIN;
CREATE TABLE IP(
    Continent        TEXT,
    Country          TEXT,
    RegionName       TEXT,
    City             TEXT,
    Lat,
    Lon,
    Isp              TEXT,
    Org              TEXT,
    AsNumber         TEXT,
    AsName           TEXT,
    Reverse          TEXT,
    MobileConnection TEXT,
    ProxyConnection  TEXT,   
    Hosting          TEXT
);
CREATE TABLE Number_phone(
    OperName    TEXT,
    Mnc         INTEGER,
    Brand       TEXT,
    Inn         INTEGER,
    Work_Mobile TEXT,
    Name        TEXT
);
CREATE TABLE MAC(
    Company    TEXT,
    Address    TEXT,
    Block_Size TEXT
);
COMMIT;""")
    except sqlite3.Error as sqlerror:
        autolog_color("error", sqlerror, "CRITICAL", wayerror=way_error_log, waygeneral=way_general_log, without_out_console=False)
    finally:
        connect.commit()
        connect.close()