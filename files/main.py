__author__ = '\nSos1ska\nhttps://github.com/Sos1ska\nhttps://vk.com/nikitasos1ska'
__code__ = '\n\nOpenSourceCode'

from typing import Any
from .important_func import load_pyc_files, delete_config, unzip_config
from .ccf import CreateCOLORconfig, CreateSYSconfig
from json import load, loads, dump, dumps
import sqlite3, datetime
import os, sys
try:
    from bs4 import BeautifulSoup
except ImportError:
    print('[ TWSEConsole ] - [ Install "bs4" -> "pip install bs4" ]')
try:
    import sqlite3
except ImportError:
    print('[ TWSEConsole ] - [ Install "sqlite3" -> "pip install pysqlite3" ]')
try:
    from LOGer import autolog_color
    from LOGer import _debug_ as debug
    from LOGer import _error_ as error
    from LOGer import _info_ as info
    from LOGer import _warning_ as warning
    from LOGer import _debug_color_ as debug_color
    from LOGer import _error_color as error_color
    from LOGer import _info_color as info_color
    from LOGer import _warning_color as warning_color
except ImportError:
    from files.core.LOGer import autolog_color as autolog_color
    autolog_color(typelog='warning', text='Not installed "LOGer", use "core.LOGer" module-{main.py}', typemsg='Important', waywarn=r'files\log\warn.log', waygeneral=r'files\log\general.log', without_out_console=False)
from ColorSos import SetColor, Work_on_win32
Work_on_win32()
try:
    from requests import get
except ImportError:
    from .core import get
    autolog_color(typelog='warning', text='Not installed "requests", use "core.requests" module-{main.py}', typemsg='Important', waywarn=r'files\log\warn.log', waygeneral=r'files\log\general.log', without_out_console=False)

Fore=SetColor.Fore
Style=SetColor.Style
Background=SetColor.BackGround
Clear=SetColor.Clear

start_list = [CreateCOLORconfig, CreateSYSconfig, unzip_config]

def _check_configs():
    if os.path.exists(r'files\config\system.json') == True:
        system = True
    elif os.path.exists(r'files\config\system.json') == False:
        system = False
    if os.path.exists(r'files\config\color.json') == True:
        color = True
    elif os.path.exists(r'files\config\color.json') == False:
        color = False
    if system == True:
        if color == True:
            return 'Configs exists'
        else:
            return 'system exists'
    else:
        if color == True:
            return 'color exists'
        else:
            return 'Configs not exists'

def clear():
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def _record_in_data_base(column, information):
    if os.path.exists(r'files\database\information.db') == True:
        pass
    elif os.path.exists(r'files\database\information.db') == False:
        with open(r'files\database\information.db', 'wb'):
            connectdb = sqlite3.connect(r'files\database\information.db')
            cur=connectdb.cursor()
            tables = ["Number_phone", "IP_Mobile", "ISP", "IP", "MAC"]
            for table in tables:
                cur.execute(f"""CREATE TABLE {table}(
                    info NULL, 
                    time NULL
                    )""")
            connectdb.commit()
            connectdb.close()
    try:
        connectdbu = sqlite3.connect(r'files\database\information.db')
    except sqlite3.OperationalError:
        autolog_color(typelog='error', text='This file does not exist', typemsg='Important', wayerror=r'files\log\error.log', waygeneral=r'files\log\general.log', without_out_console=False)
    try:
        cursor=connectdbu.cursor()
        cursor.execute(f"INSERT INTO {column} VALUES ('{information}', '{datetime.datetime.now()}')")
        connectdbu.commit()
        connectdbu.close()
    except sqlite3.Error:
        autolog_color(typelog='error', text='Error while working with database', typemsg='Important', wayerror=r'files\log\error.log', waygeneral=r'files\log\general.log', without_out_console=False)

class methods:
    class break_ip_mobile:
        class dm:
            def _rus_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                autolog_color(typelog='debug', text='Попытка - Пройдена!', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Пробить IP если он телефон' + Clear())
                autolog_color(typelog='debug', text='Вывод -> "Пробить IP если он телефон"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + '\nВведите IP-Адрес' + Clear())
                autolog_color(typelog='debug', text='Вывод -> "Введите IP-Адрес"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                ip=input('> ')
                send_request=get(f'https://htmlweb.ru/geo/api.php?ip={ip}&json')
                autolog_color(typelog='debug', text=f'Отправка запроса -> "https://htmlweb.ru/geo/api.php?ip={ip}&json"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                autolog_color(typelog='debug', text='Получение json', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                site_json=loads(soup_json)
                autolog_color(typelog='debug', text='Читаю json ответ', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                Handler=site_json
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["name"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=Handler["country"]["name"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        country = Handler["country"]["name"]
                        autolog_color(typelog='info', text=Handler["country"]["name"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=Handler["country"]["name"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        country = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["iso"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=Handler["country"]["iso"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        iso=Handler["country"]["iso"]
                        autolog_color(typelog='info', text=Handler["country"]["iso"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=Handler["country"]["iso"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        iso = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["telcod"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=Handler["country"]["telcod"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        telcod = Handler["country"]["telcod"]
                        autolog_color(typelog='info', text=Handler["country"]["telcod"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=Handler["country"]["telcod"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        iso = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["capital"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=Handler["country"]["capital"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        capital = Handler["country"]["capital"]
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        capital = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["mcc"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=Handler["country"]["mcc"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mcc = 'Not Found'
                        autolog_color(typelog='info', text=Handler["country"]["mcc"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=Handler["country"]["mcc"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mcc = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data = f'CountryIP -> {country}\nISOIP -> {iso}\nCapitalIP -> {capital} MCC -> \n{mcc}'
                    _record_in_data_base(column='IP_Mobile', information=data)
                    cont=input('')
            def _eng_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                autolog_color(typelog='debug', text='Attempt - Completed!', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Break IP if he mobile' + Clear())
                autolog_color(typelog='debug', text='Output next -> "Break IP if he mobile"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + '\nInsert IP-Address' + Clear())
                autolog_color(typelog='debug', text='Output next -> "Insert IP-Address"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                ip=input('> ')
                send_request=get(f'https://htmlweb.ru/geo/api.php?ip={ip}&json')
                autolog_color(typelog='debug', text=f'Send request -> "https://htmlweb.ru/geo/api.php?ip={ip}&json"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                autolog_color(typelog='debug', text='Get json', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                site_json=loads(soup_json)
                autolog_color(typelog='debug', text='Read json answer', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                Handler=site_json
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["name"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=Handler["country"]["name"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        country = Handler["country"]["name"]
                        autolog_color(typelog='info', text=Handler["country"]["name"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=Handler["country"]["name"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        country = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["iso"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=Handler["country"]["iso"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        iso=Handler["country"]["iso"]
                        autolog_color(typelog='info', text=Handler["country"]["iso"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=Handler["country"]["iso"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        iso = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["telcod"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=Handler["country"]["telcod"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        telcod = Handler["country"]["telcod"]
                        autolog_color(typelog='info', text=Handler["country"]["telcod"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=Handler["country"]["telcod"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        iso = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["capital"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=Handler["country"]["capital"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        capital = Handler["country"]["capital"]
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        capital = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["mcc"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=Handler["country"]["mcc"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mcc = 'Not Found'
                        autolog_color(typelog='info', text=Handler["country"]["mcc"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=Handler["country"]["mcc"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mcc = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data = f'CountryIP -> {country}\nISOIP -> {iso}\nCapitalIP -> {capital} MCC -> \n{mcc}'
                    
                    _record_in_data_base(column='IP_Mobile', information=data)
                    cont=input('')
        class without_dm:
            def _rus_(self, systemC, colorC, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Пробить IP если он телефон' + Clear())
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + '\nВведите IP-Адрес' + Clear())
                ip=input('> ')
                send_request=get(f'https://htmlweb.ru/geo/api.php?ip={ip}&json')
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json=loads(soup_json)
                Handler=site_json
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["name"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        country = Handler["country"]["name"]
                        autolog_color(typelog='info', text=Handler["country"]["name"], wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        country = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["iso"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        iso=Handler["country"]["iso"]
                        autolog_color(typelog='info', text=Handler["country"]["iso"], wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        iso = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["telcod"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        telcod = Handler["country"]["telcod"]
                        autolog_color(typelog='info', text=Handler["country"]["telcod"], wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        iso = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["capital"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        capital = Handler["country"]["capital"]
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        capital = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["mcc"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mcc = 'Not Found'
                        autolog_color(typelog='info', text=Handler["country"]["mcc"], wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mcc = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data = f'CountryIP -> {country}\nISOIP -> {iso}\nCapitalIP -> {capital} MCC -> \n{mcc}'
                    _record_in_data_base(column='IP_Mobile', information=data)
                    cont=input('')
            def _eng_(self, systemC, colorC, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=["Color Back Text"]) + 'Break IP if he mobile' + Clear())
                print(Fore(color=colorC["Color Text"]) + Background(color=["Color Back Text"]) + '\nInsert IP-Address' + Clear())
                ip=input('> ')
                send_request=get(f'https://htmlweb.ru/geo/api.php?ip={ip}&json')
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json=loads(soup_json)
                Handler=site_json
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["name"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        country = Handler["country"]["name"]
                        autolog_color(typelog='info', text=Handler["country"]["name"], wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        country = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["iso"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        iso=Handler["country"]["iso"]
                        autolog_color(typelog='info', text=Handler["country"]["iso"], wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        iso = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["telcod"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        telcod = Handler["country"]["telcod"]
                        autolog_color(typelog='info', text=Handler["country"]["telcod"], wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        iso = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["capital"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        capital = Handler["country"]["capital"]
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        capital = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"]["mcc"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mcc = 'Not Found'
                        autolog_color(typelog='info', text=Handler["country"]["mcc"], wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mcc = 'Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data = f'CountryIP -> {country}\nISOIP -> {iso}\nCapitalIP -> {capital} MCC -> \n{mcc}'
                    _record_in_data_base(column='IP_Mobile', information=data)
                    cont=input('')
        def __init__(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes, lang="RUS"or"ENG", dm="Yes"or"No"):
            if dm == "Yes":
                if lang == "RUS":
                    self.dm._rus_(self=Any, systemC=systemC, colorC=colorC, waydebug=waydebug, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
                elif lang == "ENG":
                    self.dm._eng_(self=Any, systemC=systemC, colorC=colorC, waydebug=waydebug, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
            elif dm == "No":
                if lang == "RUS":
                    self.without_dm._rus_(self=Any, systemC=systemC, colorC=colorC, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
                elif lang == "ENG":
                    self.without_dm._eng_(self=Any, systemC=systemC, colorC=colorC, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
    class get_proxy:
        class dm:
            def _rus_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                autolog_color(typelog='debug', text='Попытка - Пройдена!', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                send_request=get('https://htmlweb.ru/json/proxy/get?country=RU&perpage=5')
                autolog_color(typelog='debug', text=f'Отправка запроса -> "https://htmlweb.ru/json/proxy/get?country=RU&perpage=5"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                answer = send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                autolog_color(typelog='debug', text='Получение json', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                site_json=loads(soup_json)
                autolog_color(typelog='debug', text='Читаю json ответ', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                Handler=site_json
                try:
                    info_color(View='str', TEXT=Handler["0"]["name"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["0"]["name"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["0"]["type"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["0"]["type"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["0"]["country"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["0"]["country"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["1"]["name"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["1"]["name"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["1"]["type"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["1"]["type"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["1"]["country"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["1"]["country"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["2"]["name"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["2"]["name"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["2"]["type"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["2"]["type"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["2"]["country"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["2"]["country"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["3"]["name"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["3"]["name"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["3"]["type"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["3"]["type"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["3"]["country"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["3"]["country"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["4"]["name"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["4"]["name"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["4"]["type"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["4"]["type"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["4"]["country"], WriteTime=False)
                    autolog_color(typelog='debug', text='Использую модуль "info_color(View=\'str\', TEXT=Handler["4"]["country"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    pass
                cont=input('')
            def _eng_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                autolog_color(typelog='debug', text='Attempt - Completed!', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                send_request=get('https://htmlweb.ru/json/proxy/get?country=RU&perpage=5')
                autolog_color(typelog='debug', text=f'Send request -> "https://htmlweb.ru/json/proxy/get?country=RU&perpage=5"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                answer = send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                autolog_color(typelog='debug', text='Get json', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                site_json=loads(soup_json)
                autolog_color(typelog='debug', text='Read json answer', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                Handler=site_json
                try:
                    info_color(View='str', TEXT=Handler["0"]["name"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["0"]["name"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["0"]["type"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["0"]["type"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["0"]["country"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["0"]["country"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["1"]["name"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["1"]["name"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["1"]["type"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["1"]["type"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["1"]["country"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["1"]["country"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["2"]["name"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["2"]["name"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["2"]["type"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["2"]["type"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["2"]["country"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["2"]["country"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["3"]["name"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["3"]["name"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["3"]["type"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["3"]["type"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["3"]["country"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["3"]["country"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["4"]["name"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["4"]["name"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["4"]["type"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["4"]["type"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    info_color(View='str', TEXT=Handler["4"]["country"], WriteTime=False)
                    autolog_color(typelog='debug', text='Use module "info_color(View=\'str\', TEXT=Handler["4"]["country"], WriteTime=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    pass
                cont=input('')
        class without_dm:
            def _rus_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                send_request=get('https://htmlweb.ru/json/proxy/get?country=RU&perpage=5')
                answer = send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json=loads(soup_json)
                Handler=site_json
                try:
                    info_color(View='str', TEXT=Handler["0"]["name"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["0"]["type"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["0"]["country"], WriteTime=False)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["1"]["name"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["1"]["type"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["1"]["country"], WriteTime=False)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["2"]["name"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["2"]["type"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["2"]["country"], WriteTime=False)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["3"]["name"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["3"]["type"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["3"]["country"], WriteTime=False)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["4"]["name"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["4"]["type"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["4"]["country"], WriteTime=False)
                except KeyError:
                    pass
                cont=input('')
            def _eng_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                send_request=get('https://htmlweb.ru/json/proxy/get?country=RU&perpage=5')
                answer = send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json=loads(soup_json)
                Handler=site_json
                try:
                    info_color(View='str', TEXT=Handler["0"]["name"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["0"]["type"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["0"]["country"], WriteTime=False)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["1"]["name"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["1"]["type"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["1"]["country"], WriteTime=False)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["2"]["name"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["2"]["type"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["2"]["country"], WriteTime=False)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["3"]["name"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["3"]["type"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["3"]["country"], WriteTime=False)
                except KeyError:
                    pass
                try:
                    info_color(View='str', TEXT=Handler["4"]["name"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["4"]["type"], WriteTime=False)
                    info_color(View='str', TEXT=Handler["4"]["country"], WriteTime=False)
                except KeyError:
                    pass
                cont=input('')
        def __init__(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes, lang="RUS"or"ENG", dm="Yes"or"No"):
            if dm == "Yes":
                if lang == "RUS":
                    self.dm._rus_(self=Any, systemC=systemC, colorC=colorC, waydebug=waydebug, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
                elif lang == "ENG":
                    self.dm._eng_(self=Any, systemC=systemC, colorC=colorC, waydebug=waydebug, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
            elif dm == "No":
                if lang == "RUS":
                    self.without_dm._rus_(self=Any, systemC=systemC, colorC=colorC, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
                elif lang == "ENG":
                    self.without_dm._eng_(self=Any, systemC=systemC, colorC=colorC, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
    class break_number:
        class dm:
            def _rus_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                autolog_color(typelog='debug', text=f'Попытка - Пройдена!', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Пробить номер телефона' + Clear())
                autolog_color(typelog='debug', text='Вывод -> "Пробить номер телефона"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Введите номер телефона' + Clear())
                autolog_color(typelog='debug', text='Вывод -> "Введите номер телефона"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                number=input('> ')
                send_request=get(f'https://htmlweb.ru/json/mnp/phone/{number}')
                autolog_color(typelog='debug', text=f'Отправка запроса -> "https://htmlweb.ru/json/mnp/phone/{number}"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                autolog_color(typelog='debug', text='Получение json', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                site_json=loads(soup_json)
                autolog_color(typelog='debug', text='Читаю json ответ', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                Handler=site_json
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["oper"]["name"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["oper"]["name"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        name=Handler["oper"]["name"]
                        autolog_color(typelog='info', text=Handler["oper"]["name"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["oper"]["name"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        name='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='mnc> '+str(Handler["oper"]["mnc"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'mnc> \'+Handler["oper"]["mnc"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mnc=Handler["oper"]["mnc"]
                        autolog_color(typelog='info', text='mnc> '+str(Handler["oper"]["mnc"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль ->ip "autolog_color(typelog=\'info\', text=\'mnc> \'+Handler["oper"]["mnc"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mnc='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["oper"]["brand"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["oper"]["brand"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        brand=Handler["oper"]["brand"]
                        autolog_color(typelog='info', text=Handler["oper"]["brand"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["oper"]["brand"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        brand='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='inn> '+str(Handler["oper"]["inn"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'mnc> \'+Handler["oper"]["inn"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        inn=Handler["oper"]["inn"]
                        autolog_color(typelog='info', text='inn> '+str(Handler["oper"]["inn"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'inn> \'+Handler["oper"]["inn"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        inn='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='work> '+str(Handler["mobile"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'work> \'+Handler["mobile"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mobile=Handler["mobile"]
                        autolog_color(typelog='info', text='work> '+str(Handler["mobile"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'work> \'+Handler["mobile"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mobile='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data=f"Name ->{name},\n mnc -> {mnc},\nbrand -> {brand},\ninn -> {inn},\nmobile -> {mobile}"
                    _record_in_data_base(column='Number_phone', information=data)
                    cont=input('')
            def _eng_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                autolog_color(typelog='debug', text=f'Attempt - Completed!', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Break Number Phone' + Clear())
                autolog_color(typelog='debug', text='Out -> "Break Number Phone"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Enter Number Phone' + Clear())
                autolog_color(typelog='debug', text='Out -> "Enter Number Phone"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                number=input('> ')
                send_request=get(f'https://htmlweb.ru/json/mnp/phone/{number}')
                autolog_color(typelog='debug', text=f'Send request -> "https://htmlweb.ru/json/mnp/phone/{number}"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                autolog_color(typelog='debug', text='Get json', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                site_json=loads(soup_json)
                autolog_color(typelog='debug', text='Read json answer', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                Handler=site_json
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["oper"]["name"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["oper"]["name"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        name=Handler["oper"]["name"]
                        autolog_color(typelog='info', text=Handler["oper"]["name"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["oper"]["name"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        name='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='mnc> '+str(Handler["oper"]["mnc"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'mnc> \'+Handler["oper"]["mnc"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mnc=Handler["oper"]["mnc"]
                        autolog_color(typelog='info', text='mnc> '+str(Handler["oper"]["mnc"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'mnc> \'+Handler["oper"]["mnc"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mnc='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["oper"]["brand"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["oper"]["brand"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        brand=Handler["oper"]["brand"]
                        autolog_color(typelog='info', text=Handler["oper"]["brand"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["oper"]["brand"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        brand='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='inn> '+str(Handler["oper"]["inn"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'mnc> \'+Handler["oper"]["inn"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        inn=Handler["oper"]["inn"]
                        autolog_color(typelog='info', text='inn> '+str(Handler["oper"]["inn"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'inn> \'+Handler["oper"]["inn"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        inn='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='work> '+str(Handler["mobile"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'work> \'+Handler["mobile"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mobile=Handler["mobile"]
                        autolog_color(typelog='info', text='work> '+str(Handler["mobile"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'work> \'+Handler["mobile"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mobile='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data=f"Name ->{name},\n mnc -> {mnc},\nbrand -> {brand},\ninn -> {inn},\nmobile -> {mobile}"
                    _record_in_data_base(column='Number_phone', information=data)
                    cont=input('')
        class without_dm:
            def _rus_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Пробить номер телефона' + Clear())
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Введите номер телефона' + Clear())
                number=input('> ')
                send_request=get(f'https://htmlweb.ru/json/mnp/phone/{number}')
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json=loads(soup_json)
                Handler=site_json
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["oper"]["name"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        name=Handler["oper"]["name"]
                        autolog_color(typelog='info', text=Handler["oper"]["name"], wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        name='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='mnc> '+str(Handler["oper"]["mnc"]), wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mnc=Handler["oper"]["mnc"]
                        autolog_color(typelog='info', text='mnc> '+str(Handler["oper"]["mnc"]), wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mnc='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["oper"]["brand"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        brand=Handler["oper"]["brand"]
                        autolog_color(typelog='info', text=Handler["oper"]["brand"], wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        brand='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='inn> '+str(Handler["oper"]["inn"]), wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        inn=Handler["oper"]["inn"]
                        autolog_color(typelog='info', text='inn> '+str(Handler["oper"]["inn"]), wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        inn='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='work> '+str(Handler["mobile"]), wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mobile=Handler["mobile"]
                        autolog_color(typelog='info', text='work> '+str(Handler["mobile"]), wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mobile='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data=f"Name ->{name},\n mnc -> {mnc},\nbrand -> {brand},\ninn -> {inn},\nmobile -> {mobile}"
                    _record_in_data_base(column='Number_phone', information=data)
                    cont=input('')
            def _eng_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Break Number Phone' + Clear())
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Enter Number Phone' + Clear())
                number=input('> ')
                send_request=get(f'https://htmlweb.ru/json/mnp/phone/{number}')
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json=loads(soup_json)
                Handler=site_json
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["oper"]["name"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        name=Handler["oper"]["name"]
                        autolog_color(typelog='info', text=Handler["oper"]["name"], wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        name='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='mnc> '+str(Handler["oper"]["mnc"]), wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mnc=Handler["oper"]["mnc"]
                        autolog_color(typelog='info', text='mnc> '+str(Handler["oper"]["mnc"]), wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mnc='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["oper"]["brand"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        brand=Handler["oper"]["brand"]
                        autolog_color(typelog='info', text='mnc> '+str(Handler["oper"]["mnc"]), wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        brand='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='inn> '+str(Handler["oper"]["inn"]), wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        inn=Handler["oper"]["inn"]
                        autolog_color(typelog='info', text='inn> '+str(Handler["oper"]["inn"]), wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        inn='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='work> '+str(Handler["mobile"]), wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mobile=Handler["mobile"]
                        autolog_color(typelog='info', text='work> '+str(Handler["mobile"]), wayinfo=wayinfo, without_out_console=False)
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        mobile='Not Found'
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data=f"Name ->{name},\n mnc -> {mnc},\nbrand -> {brand},\ninn -> {inn},\nmobile -> {mobile}"
                    _record_in_data_base(column='Number_phone', information=data)
                    cont=input('')
        def __init__(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes, lang="RUS"or"ENG", dm="Yes"or"No"):
            if dm == "Yes":
                if lang == "RUS":
                    self.dm._rus_(self=Any, systemC=systemC, colorC=colorC, waydebug=waydebug, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
                elif lang == "ENG":
                    self.dm._eng_(self=Any, systemC=systemC, colorC=colorC, waydebug=waydebug, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
            elif dm == "No":
                if lang == "RUS":
                    self.without_dm._rus_(self=Any, systemC=systemC, colorC=colorC, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
                elif lang == "ENG":
                    self.without_dm._eng_(self=Any, systemC=systemC, colorC=colorC, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
    class break_ip:
        class dm:
            def _rus_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                autolog_color(typelog='debug', text='Попытка - Пройдена!', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Пробить IP-Адрес' + Clear())
                autolog_color(typelog='debug', text='Вывод -> "Пробить IP-Адрес"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Введите IP-Адрес' + Clear())
                autolog_color(typelog='debug', text='Вывод -> "Введите IP-Адрес"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                ip=input('> ')
                send_request=get(f"http://ip-api.com/json/{ip}")
                autolog_color(typelog='debug', text=f'Оправка запроса -> "http://ip-api.com/json/{ip}"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                autolog_color(typelog='debug', text='Получение json', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                site_json=loads(soup_json)
                autolog_color(typelog='debug', text='Читаю json ответ', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                Handler=site_json
                try:    
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["country"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["country"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["country"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        country=Handler["country"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        country='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["regionName"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["regionName"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["regionName"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["regionName"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        region=Handler["regionName"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        region='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["city"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["city"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["city"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["city"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        city=Handler["city"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        city='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["as"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["as"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["as"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["as"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        asb=Handler["as"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        asb='Not Found'
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data=f"Country ->{country},\nregion -> {region},\ncity -> {city},\nas -> {asb}"
                    _record_in_data_base(column='IP', information=data)
                    cont=input('')
            def _eng_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                autolog_color(typelog='debug', text='Attempt - Completed!', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Break IP-Address' + Clear())
                autolog_color(typelog='debug', text='Out -> "Break IP-Address"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Enter IP-Address' + Clear())
                autolog_color(typelog='debug', text='Out -> "Enter IP-Address"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                ip=input('> ')
                send_request=get(f"http://ip-api.com/json/{ip}")
                autolog_color(typelog='debug', text=f'Send request -> "http://ip-api.com/json/{ip}"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                autolog_color(typelog='debug', text='Get json', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                site_json=loads(soup_json)
                autolog_color(typelog='debug', text='Read json answer', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                Handler=site_json
                try:    
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["country"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["country"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["country"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        country=Handler["country"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        country='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["regionName"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["regionName"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["regionName"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["regionName"], wayinfo=wayinfo, without_out_console=False)"')
                        region=Handler["regionName"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        region='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["city"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["city"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["city"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["city"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        city=Handler["city"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        city='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["as"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["as"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["as"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["as"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        asb=Handler["as"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        asb='Not Found'
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data=f"Country ->{country},\nregion -> {region},\ncity -> {city},\nas -> {asb}"
                    _record_in_data_base(column='IP', information=data)
                    cont=input('')
        class without_dm:
            def _rus_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Пробить IP-Адрес' + Clear())
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Введите IP-Адрес' + Clear())
                ip=input('> ')
                send_request=get(f"http://ip-api.com/json/{ip}")
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json=loads(soup_json)
                Handler=site_json
                try:    
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["country"], wayinfo=wayinfo, without_out_console=False)
                        country=Handler["country"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        country='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["regionName"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["regionName"], wayinfo=wayinfo, without_out_console=False)
                        region=Handler["regionName"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        region='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["city"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["city"], wayinfo=wayinfo, without_out_console=False)
                        city=Handler["city"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        city='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["as"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["as"], wayinfo=wayinfo, without_out_console=False)
                        asb=Handler["as"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        asb='Not Found'
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data=f"Country ->{country},\nregion -> {region},\ncity -> {city},\nas -> {asb}"
                    _record_in_data_base(column='IP', information=data)
                    cont=input('')
            def _eng_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Break IP-Address' + Clear())
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Enter IP-Address' + Clear())
                ip=input('> ')
                send_request=get(f"http://ip-api.com/json/{ip}")
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json=loads(soup_json)
                Handler=site_json
                try:    
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["country"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["country"], wayinfo=wayinfo, without_out_console=False)
                        country=Handler["country"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        country='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["regionName"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["regionName"], wayinfo=wayinfo, without_out_console=False)
                        region=Handler["regionName"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        region='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["city"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["city"], wayinfo=wayinfo, without_out_console=False)
                        city=Handler["city"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        city='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["as"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["as"], wayinfo=wayinfo, without_out_console=False)
                        asb=Handler["as"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        asb='Not Found'
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data=f"Country ->{country},\nregion -> {region},\ncity -> {city},\nas -> {asb}"
                    _record_in_data_base(column='IP', information=data)
                    cont=input('')
        def __init__(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes, lang="RUS"or"ENG", dm="Yes"or"No"):
            if dm == "Yes":
                if lang == "RUS":
                    self.dm._rus_(self=Any, systemC=systemC, colorC=colorC, waydebug=waydebug, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
                elif lang == "ENG":
                    self.dm._eng_(self=Any, systemC=systemC, colorC=colorC, waydebug=waydebug, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
            elif dm == "No":
                if lang == "RUS":
                    self.without_dm._rus_(self=Any, systemC=systemC, colorC=colorC, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
                elif lang == "ENG":
                    self.without_dm._eng_(self=Any, systemC=systemC, colorC=colorC, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
    class break_mac:
        class dm:
            def _rus_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                autolog_color(typelog='debug', text='Попытка - Пройдена!', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Пробить MAC-Адрес' + Clear())
                autolog_color(typelog='debug', text='Вывод -> "Пробить MAC-Адрес"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Введите MAC-Адрес' + Clear())
                autolog_color(typelog='debug', text='Вывод -> "Введите MAC-Адрес"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                mac=input('> ')
                send_request=get(f'https://api.2ip.ua/mac.json?mac={mac}')
                autolog_color(typelog='debug', text=f'Отправка запроса -> "https://api.2ip.ua/mac.json?mac={mac}"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                autolog_color(typelog='debug', text='Получение json', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                site_json=loads(soup_json)
                autolog_color(typelog='debug', text='Читаю json ответ', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                Handler=site_json
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["company"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["company"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["company"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["company"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        company=Handler["company"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        company='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["address"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["address"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["address"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=Handler["address"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        address=Handler["address"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        address='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Block-Size'+str(Handler["block_size"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Block-Size\'+str(Handler["block_size"]), wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Block-Size'+str(Handler["block_size"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Block-Size\'+str(Handler["block_size"]), wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        block_size=Handler["block_size"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Использую модуль -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        block_size='Not Found'
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data=f"Company ->{company},\naddress -> {address},\nblock_size -> {block_size}"
                    _record_in_data_base(column='MAC', information=data)
                    cont=input('')
            def _eng_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                autolog_color(typelog='debug', text='Attempt - Completed!', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Break MAC-Address' + Clear())
                autolog_color(typelog='debug', text='Out -> "Break MAC-Address"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Enter MAC-Address' + Clear())
                autolog_color(typelog='debug', text='Out -> "Enter MAC-Address"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                mac=input('> ')
                send_request=get(f'https://api.2ip.ua/mac.json?mac={mac}')
                autolog_color(typelog='debug', text=f'Send request -> "https://api.2ip.ua/mac.json?mac={mac}"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                autolog_color(typelog='debug', text='Get json', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                site_json=loads(soup_json)
                autolog_color(typelog='debug', text='Read json answer', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                Handler=site_json
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["company"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["company"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["company"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["company"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        company=Handler["company"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        company='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["address"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["address"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["address"], wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=Handler["address"], wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        address=Handler["address"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        address='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Block-Size'+str(Handler["block_size"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Block-Size\'+str(Handler["block_size"]), wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Block-Size'+str(Handler["block_size"]), wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Block-Size\'+str(Handler["block_size"]), wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        block_size=Handler["block_size"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        autolog_color(typelog='debug', text='Use module -> "autolog_color(typelog=\'info\', text=\'Not Found\', wayinfo=wayinfo, without_out_console=False)"', waydebug=waydebug, waygeneral=waygeneral, without_out_console=True)
                        block_size='Not Found'
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data=f"Company ->{company},\naddress -> {address},\nblock_size -> {block_size}"
                    _record_in_data_base(column='MAC', information=data)
                    cont=input('')
        class without_dm:
            def _rus_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Пробить MAC-Адрес' + Clear())
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Введите MAC-Адрес' + Clear())
                mac=input('> ')
                send_request=get(f'https://api.2ip.ua/mac.json?mac={mac}')
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json=loads(soup_json)
                Handler=site_json
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["company"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["company"], wayinfo=wayinfo, without_out_console=False)
                        company=Handler["company"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        company='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["address"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["address"], wayinfo=wayinfo, without_out_console=False)
                        address=Handler["address"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        address='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Block-Size'+str(Handler["block_size"]), wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Block-Size'+str(Handler["block_size"]), wayinfo=wayinfo, without_out_console=False)
                        block_size=Handler["block_size"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        block_size='Not Found'
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data=f"Company ->{company},\naddress -> {address},\nblock_size -> {block_size}"
                    _record_in_data_base(column='MAC', information=data)
                    cont=input('')
            def _eng_(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes):
                if systemC["Clear Every Time"] == "No":
                    pass
                elif systemC["Clear Every Time"] == "Yes":
                    clear()
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Break MAC-Address' + Clear())
                print(Fore(color=colorC["Color Text"]) + Background(color=colorC["Color Back Text"]) + 'Enter MAC-Address' + Clear())
                mac=input('> ')
                send_request=get(f'https://api.2ip.ua/mac.json?mac={mac}')
                answer=send_request
                soup_json=BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json=loads(soup_json)
                Handler=site_json
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["company"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["company"], wayinfo=wayinfo, without_out_console=False)
                        company=Handler["company"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        company='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text=Handler["address"], wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text=Handler["address"], wayinfo=wayinfo, without_out_console=False)
                        address=Handler["address"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        address='Not Found'
                try:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Block-Size'+str(Handler["block_size"]), wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Block-Size'+str(Handler["block_size"]), wayinfo=wayinfo, without_out_console=False)
                        block_size=Handler["block_size"]
                except KeyError:
                    if systemC["Record Info in DataBase"] == "No":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                    elif systemC["Record Info in DataBase"] == "Yes":
                        autolog_color(typelog='info', text='Not Found', wayinfo=wayinfo, without_out_console=False)
                        block_size='Not Found'
                if systemC["Record Info in DataBase"] == "No":
                    cont=input('')
                elif systemC["Record Info in DataBase"] == "Yes":
                    data=f"Company ->{company},\naddress -> {address},\nblock_size -> {block_size}"
                    _record_in_data_base(column='MAC', information=data)
                    cont=input('')
        def __init__(self, systemC, colorC, waydebug=bytes, wayerror=bytes, waywarning=bytes, waygeneral=bytes, wayinfo=bytes, lang="RUS"or"ENG", dm="Yes"or"No"):
            if dm == "Yes":
                if lang == "RUS":
                    self.dm._rus_(self=Any, systemC=systemC, colorC=colorC, waydebug=waydebug, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
                elif lang == "ENG":
                    self.dm._eng_(self=Any, systemC=systemC, colorC=colorC, waydebug=waydebug, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
            elif dm == "No":
                if lang == "RUS":
                    self.without_dm._rus_(self=Any, systemC=systemC, colorC=colorC, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)
                elif lang == "ENG":
                    self.without_dm._eng_(self=Any, systemC=systemC, colorC=colorC, wayerror=wayerror, waywarning=waywarning, waygeneral=waygeneral, wayinfo=wayinfo)

class _console:
    def __choice__(self):
        with open(r'files\config\system.json') as file_system:
            data=load(file_system)
        with open(r'files\config\color.json') as file_color:
            data_color=load(file_color)
        with open(r'files\config\user.json') as file_user:
            data_user=load(file_user)
        autolog_color(typelog='debug', text='Attempt - Completed!', waydebug=data["Ways"]["debug"], waygeneral=data["Ways"]["general"])
        while True:
            choice=input(f'{data_user["UserName"]}{data_user["ProgramName"]}> ')
            if choice == "break_ip_mobile":
                if data_user["Language"] == "RUS":
                    methods.break_ip_mobile(systemC=data, colorC=data_color, waydebug=data["Ways"]["debug"], wayerror=data["Ways"]["error"], wayinfo=data["Ways"]["info"], waywarning=data["Ways"]["warning"], waygeneral=data["Ways"]["general"], dm=data["DebugMode"], lang="RUS")
                elif data_user["Language"] == "ENG":
                    methods.break_ip_mobile(systemC=data, colorC=data_color, waydebug=data["Ways"]["debug"], wayerror=data["Ways"]["error"], wayinfo=data["Ways"]["info"], waywarning=data["Ways"]["warning"], waygeneral=data["Ways"]["general"], dm=data["DebugMode"], lang="ENG")
            elif choice == "get_proxy":
                if data_user["Language"] == "RUS":
                    methods.get_proxy(systemC=data, colorC=data_color, waydebug=data["Ways"]["debug"], wayerror=data["Ways"]["error"], wayinfo=data["Ways"]["info"], waywarning=data["Ways"]["warning"], waygeneral=data["Ways"]["general"], dm=data["DebugMode"], lang="RUS")
                elif data_user["Language"] == "ENG":
                    methods.get_proxy(systemC=data, colorC=data_color, waydebug=data["Ways"]["debug"], wayerror=data["Ways"]["error"], wayinfo=data["Ways"]["info"], waywarning=data["Ways"]["warning"], waygeneral=data["Ways"]["general"], dm=data["DebugMode"], lang="ENG")
            elif choice == "break_number_phone":
                if data_user["Language"] == "RUS":
                    methods.break_number(systemC=data, colorC=data_color, waydebug=data["Ways"]["debug"], wayerror=data["Ways"]["error"], wayinfo=data["Ways"]["info"], waywarning=data["Ways"]["warning"], waygeneral=data["Ways"]["general"], dm=data["DebugMode"], lang="RUS")
                elif data_user["Language"] == "ENG":
                    methods.break_number(systemC=data, colorC=data_color, waydebug=data["Ways"]["debug"], wayerror=data["Ways"]["error"], wayinfo=data["Ways"]["info"], waywarning=data["Ways"]["warning"], waygeneral=data["Ways"]["general"], dm=data["DebugMode"], lang="ENG")
            elif choice == "break_ip":
                if data_user["Language"] == "RUS":
                    methods.break_ip(systemC=data, colorC=data_color, waydebug=data["Ways"]["debug"], wayerror=data["Ways"]["error"], wayinfo=data["Ways"]["info"], waywarning=data["Ways"]["warning"], waygeneral=data["Ways"]["general"], dm=data["DebugMode"], lang="RUS")
                elif data_user["Language"] == "ENG":
                    methods.break_ip(systemC=data, colorC=data_color, waydebug=data["Ways"]["debug"], wayerror=data["Ways"]["error"], wayinfo=data["Ways"]["info"], waywarning=data["Ways"]["warning"], waygeneral=data["Ways"]["general"], dm=data["DebugMode"], lang="ENG")
            elif choice == "exit":
                quit()
    def __main__(self):
        if _check_configs() == 'Configs exists':
            pass
        elif _check_configs() == 'color exists' or 'system exists' or 'Configs not exists':
            for start in start_list:
                start(record=True)
        with open(r'files\config\system.json') as file_system:
            data=load(file_system)
        with open(r'files\config\color.json') as file_color:
            data_color=load(file_color)
        with open(r'files\config\user.json') as file_user:
            data_user=load(file_user)
        if data["Start Clear Window"] == "Yes": clear()
        elif data["Start Clear Window"] == "No": pass
        if data["Start Show Banner"] == "Yes":
            try:
                with open(r'files\%s' % (data_user["LoadBanner"]["way1"]), 'r') as banner: banner.seek(0), print(Fore(color=data_color["Color Banner"], skip_error=False) + Background(color=data_color["Color Back Banner"], skip_error=False) + banner.read() + Clear())
            except FileNotFoundError:
                autolog_color(typelog='warning', text='Not Found File -> %s' % (data_user["LoadBanner"]["way1"]), waywarn=data["Ways"]["warning"], waygeneral=data["Ways"]["general"], without_out_console=False)
                try:
                    with open(r'files\%s' % (data_user["LoadBanner"]["way2"]), 'r') as banner: banner.seek(0), print(Fore(color=data_color["Color Banner"], skip_error=False) + Background(color=data_color["Color Back Banner"], skip_error=False) + banner.read() + Clear())
                except FileNotFoundError:
                    autolog_color(typelog='error', text='Not Found File -> %s' % (data_user["LoadBanner"]["way2"]), wayerror=str(data["Ways"]["error"]), waygeneral=str(data["Ways"]["general"]), without_out_console=False)
                    quit()
                autolog_color(typelog='debug', text='Trying call "__choice__"', waydebug=data["Ways"]["debug"], waygeneral=data["Ways"]["general"], without_out_console=True)
                try: self.__choice__()
                except AttributeError: _console.__choice__(Any)
            autolog_color(typelog='debug', text='Trying call "__choice__"', waydebug=data["Ways"]["debug"], waygeneral=data["Ways"]["general"], without_out_console=True)
            _console.__choice__(Any)
        elif data["Start Show Banner"] == "No":
            pass
        autolog_color(typelog='debug', text='Trying call "__choice__"', waydebug=data["Ways"]["debug"], waygeneral=["Ways"]["general"], without_out_console=True)
        try: self.__choice__()
        except AttributeError: _console.__choice__(Any)
