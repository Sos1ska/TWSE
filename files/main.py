__author__ = '\nSos1ska\nhttps://github.com/Sos1ska\nhttps://vk.com/nikitasos1ska'
__code__ = '\n\nOpenSourceCode'

import os, sys, json, sqlite3
from typing import Any
try : from TWSE_FUP import BreakNumber, BreakMACAddress, BreakIPAddress
except ImportError: 
    try : from .core import BreakNumber, BreakMACAddress, BreakIPAddress
    except ImportError:
        match os.sys.platform:
            case "win32":
                match os.path.exists(r'files\core\TWSE_FUP\__init__.py'):
                    case True:
                        print('[ TWSEConsole ] - [ Local package damaged! ]')
                        quit()
                    case False:
                        print('[ TWSEConsole ] - [ Local package not exists! ]')
                        quit()
            case _:
                match os.path.exists(r'files/core/TWSE_FUP/__init__.py'):
                    case True:
                        print('[ TWSEConsole ] - [ Local package damaged! ]')
                        quit()
                    case False:
                        print('[ TWSEConsole ] - [ Local package not exists! ]')
                        quit()
try : from LOGer import autolog_color
except ImportError: 
    try : from .core import autolog_color
    except ImportError:
        match os.sys.platform:
            case "win32":
                match os.path.exists(r'files\core\LOGer\__init__.py'):
                    case True:
                        print('[ TWSEConsole ] - [ Local package damaged! ]')
                        quit()
                    case False:
                        print('[ TWSEConsole ] - [ Local package not exists! ]')
                        quit()
            case _:
                match os.path.exists(r'files/core/LOGer/__init__.py'):
                    case True:
                        print('[ TWSEConsole ] - [ Local package damaged! ]')
                        quit()
                    case False:
                        print('[ TWSEConsole ] - [ Local package not exists! ]')
                        quit()
try : from files.important_func import *
except ImportError:
    match os.sys.platform:
        case "win32":
            match os.path.exists(r'files\important_func.py'):
                case True:
                    print('[ TWSEConsole ] - [ Local package damaged! ]')
                    quit()
                case False:
                    print('[ TWSEConsole ] - [ Local package not exists! ]')
                    quit()
        case _:
            match os.path.exists(r'files/important_func.py'):
                case True:
                    print('[ TWSEConsole ] - [ Local package damaged! ]')
                    quit()
                case False:
                    print('[ TWSEConsole ] - [ Local package not exists! ]')
                    quit()
try : from files.ccf import *
except ImportError:
    match os.sys.platform:
        case "win32":
            match os.path.exists(r'files\ccf.py'):
                case True:
                    print('[ TWSEConsole ] - [ Local package damaged! ]')
                    quit()
                case False:
                    print('[ TWSEConsole ] - [ Local package not exists! ]')
                    quit()
        case _:
            match os.path.exists(r'files/ccf.py'):
                case True:
                    print('[ TWSEConsole ] - [ Local package damaged! ]')
                    quit()
                case False:
                    print('[ TWSEConsole ] - [ Local package not exists! ]')
                    quit()
try : from files.create_database import _create
except ImportError:
    match os.sys.platform:
        case "win32":
            match os.path.exists(r'files\create_database.py'):
                case True:
                    print('[ TWSEConsole ] - [ Local package damaged! ]')
                    quit()
                case False:
                    print('[ TWSEConsole ] - [ Local package not exists! ]')
                    quit()
        case _:
            match os.path.exists(r'files/create_database.py'):
                case True:
                    print('[ TWSEConsole ] - [ Local package damaged! ]')
                    quit()
                case False:
                    print('[ TWSEConsole ] - [ Local package not exists! ]')
                    quit()
try : from files.record_database import _insert
except ImportError:
    match os.sys.platform:
        case "win32":
            match os.path.exists(r'files\record_database.py'):
                case True:
                    print('[ TWSEConsole ] - [ Local package damaged! ]')
                    quit()
                case False:
                    print('[ TWSEConsole ] - [ Local package not exists! ]')
                    quit()
        case _:
            match os.path.exists(r'files/record_database.py'):
                case True:
                    print('[ TWSEConsole ] - [ Local package damaged! ]')
                    quit()
                case False:
                    print('[ TWSEConsole ] - [ Local package not exists! ]')
                    quit()

def clear():
    match os.sys.platform:
        case "win32":
            os.system("cls")
        case _:
            os.system("clear")

class Exceptions:
    class NotFoundParameters(Exception): ...

class Config:
    try:
        with open('%s' % (path_os(r'files/config/system.json')), 'r') as system_json : system=json.load(system_json)
    except FileNotFoundError : CreateSYSconfig(record=True), unzip_config(True), print('[ TWSEConsole ] - [ Restart program. I create system.json')
    try:
        with open('%s' % (path_os(r'files/config/user.json')), 'r') as user_json : user=json.load(user_json)
    except FileNotFoundError : CreateUSERconfig(record=True), unzip_config(True), print('[ TWSEConsole ] - [ Restart program. I create user.json')

class Methods:
    class ip:
        def __init__(self, lang):
            autolog_color(typelog='debug', text='Attempt - Completed!', waydebug='%s' % (path_os(Config.system["Ways"]["debug"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), without_out_console=True)
            match lang:
                case "RUS":
                    match Config.system["Clear Every Time"]:
                        case "Yes" : clear()
                        case "No" : pass
                    print('Введите MAC-Адрес')
                    IP=input('> ')
                    BreakIPAddress(mode="JSON", ip=IP, way='%s' % (path_os(r'files/cache/ip.json')), debug=True).main()
                    with open('%s' % (path_os(r'files/cache/ip.json')), 'r') as ip_json : data=json.load(ip_json)
                    autolog_color(typelog='info', text="Continent > "+data["Continent"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Country > "+data["Country"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="RegionName > "+data["RegionName"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="City > "+data["City"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Lat > "+data["Lat"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Lon > "+data["Lon"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="ISP > "+data["ISP"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="ORG > "+data["ORG"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="AS > "+data["AS"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="ASName > "+data["ASName"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Reverse > "+data["Reverse"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="MobileConnection > "+data["MobileConnection"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="ProxyConnection > "+data["ProxyConnection"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Hosting > "+data["Hosting"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    match Config.system["Record Info in DataBase"]:
                        case "Yes" : _insert('%s' % (path_os(Config.system["DataBase"]["Way"]+Config.system["DataBase"]["Name"])), 'IP', 
                                            data["Continent"], 
                                            data["Country"], 
                                            data["RegionName"], 
                                            data["City"], 
                                            data["Lat"], 
                                            data["Lon"], 
                                            data["ISP"], 
                                            data["ORG"], 
                                            data["AS"], 
                                            data["ASName"], 
                                            data["Reverse"], 
                                            data["MobileConnection"], 
                                            data["ProxyConnection"], 
                                            data["Hosting"])
                        case "No" : pass
                    cont=input('')
                case "ENG":
                    match Config.system["Clear Every Time"]:
                        case "Yes" : clear()
                        case "No" : pass
                    print('Enter MAC-Address')
                    IP=input('> ')
                    BreakIPAddress(mode="JSON", ip=IP, way='%s' % (path_os(r'files/cache/ip.json')), debug=True).main()
                    with open('%s' % (path_os(r'files/cache/ip.json')), 'r') as ip_json : data=json.load(ip_json)
                    autolog_color(typelog='info', text="Continent > "+data["Continent"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Country > "+data["Country"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="RegionName > "+data["RegionName"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="City > "+data["City"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Lat > "+data["Lat"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Lon > "+data["Lon"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="ISP > "+data["ISP"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="ORG > "+data["ORG"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="AS > "+data["AS"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="ASName > "+data["ASName"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Reverse > "+data["Reverse"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="MobileConnection > "+data["MobileConnection"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="ProxyConnection > "+data["ProxyConnection"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Hosting > "+data["Hosting"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    match Config.system["Record Info in DataBase"]:
                        case "Yes":
                            try:_insert('%s' % (path_os(Config.system["DataBase"]["Way"]+Config.system["DataBase"]["Name"])), 'IP', 
                                            data["Continent"], 
                                            data["Country"], 
                                            data["RegionName"], 
                                            data["City"], 
                                            data["Lat"], 
                                            data["Lon"], 
                                            data["ISP"], 
                                            data["ORG"], 
                                            data["AS"], 
                                            data["ASName"], 
                                            data["Reverse"], 
                                            data["MobileConnection"], 
                                            data["ProxyConnection"], 
                                            data["Hosting"])
                            except sqlite3.OperationalError: _create(path_os(Config.system["DataBase"]["Way"]+Config.system["DataBase"]["Name"]), path_os(Config.system["Ways"]["error"]), path_os(Config.system["Ways"]["general"]))
                        case "No" : pass
                    cont=input('')
                case _ : raise Exceptions.NotFoundParameters("-> %s?" % (lang))
    class number:
        def __init__(self, lang):
            autolog_color(typelog='debug', text='Attempt - Completed!', waydebug='%s' % (path_os(Config.system["Ways"]["debug"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), without_out_console=True)
            match lang:
                case "RUS":
                    match Config.system["Clear Every Time"]:
                        case "Yes" : clear()
                        case "No" : pass
                    print('Введите MAC-Адрес')
                    NUMBER=input('> ')
                    BreakNumber(mode="JSON", number=NUMBER, way='%s' % (path_os(r'files/cache/numberphone.json')), debug=True).main()
                    with open('%s' % (path_os(r'files/cache/numberphone.json')), 'r') as number_json : data=json.load(number_json)
                    autolog_color(typelog='info', text="OperName > "+data["Opername"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="MNC > "+data["MNC"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Brand > "+data["Brand"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="INN > "+data["INN"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Work_Mobile > "+data["Work_Mobile"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Name > "+data["Name"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    match Config.system["Record Info in DataBase"]:
                        case "Yes" : _insert('%s' % (path_os(Config.system["DataBase"]["Way"]+Config.system["DataBase"]["Name"])), 'Number', 
                                            data["Opername"], 
                                            data["MNC"], 
                                            data["Brand"], 
                                            data["INN"], 
                                            data["Work_Mobile"], 
                                            data["Name"])
                        case "No" : pass
                    cont=input('')
                case "ENG":
                    match Config.system["Clear Every Time"]:
                        case "Yes" : clear()
                        case "No" : pass
                    print('Enter MAC-Address')
                    NUMBER=input('> ')
                    BreakNumber(mode="JSON", number=NUMBER, way='%s' % (path_os(r'files/cache/numberphone.json')), debug=True).main()
                    with open('%s' % (path_os(r'files/cache/numberphone.json')), 'r') as number_json : data=json.load(number_json)
                    autolog_color(typelog='info', text="OperName > "+data["Opername"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="MNC > "+data["MNC"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Brand > "+data["Brand"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="INN > "+data["INN"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Work_Mobile > "+data["Work_Mobile"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Name > "+data["Name"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    match Config.system["Record Info in DataBase"]:
                        case "Yes" : _insert('%s' % (path_os(Config.system["DataBase"]["Way"]+Config.system["DataBase"]["Name"])), 'Number', 
                                            data["Opername"], 
                                            data["MNC"], 
                                            data["Brand"], 
                                            data["INN"], 
                                            data["Work_Mobile"], 
                                            data["Name"])
                        case "No" : pass
                    cont=input('')
                case _ : raise Exceptions.NotFoundParameters("-> %s?" % (lang))
    class mac:
        def __init__(self, lang):
            autolog_color(typelog='debug', text='Attempt - Completed!', waydebug='%s' % (path_os(Config.system["Ways"]["debug"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), without_out_console=True)
            match lang:
                case "RUS":
                    match Config.system["Clear Every Time"]:
                        case "Yes" : clear()
                        case "No" : pass
                    print('Введите MAC-Адрес')
                    MAC=input('> ')
                    BreakMACAddress(mode="JSON", mac=MAC, way='%s' % (path_os(r'files/cache/macaddress.json')), debug=True).main()
                    with open('%s' % (path_os(r'files/cache/macaddress.json')), 'r') as mac_json : data=json.load(mac_json)
                    autolog_color(typelog='info', text="Company > "+data["Company"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Address > "+data["Address"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Block_Size > "+data["BlockSize"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    match Config.system["Record Info in DataBase"]:
                        case "Yes" : _insert('%s' % (path_os(Config.system["DataBase"]["Way"]+Config.system["DataBase"]["Name"])), 'MAC', 
                                            data["Company"], 
                                            data["Address"], 
                                            data["BlockSize"])
                        case "No" : pass
                    cont=input('')
                case "ENG":
                    match Config.system["Clear Every Time"]:
                        case "Yes" : clear()
                        case "No" : pass
                    print('Enter MAC-Address')
                    MAC=input('> ')
                    BreakMACAddress(mode="JSON", mac=MAC, way='%s' % (path_os(r'files/cache/macaddress.json')), debug=True).main()
                    with open('%s' % (path_os(r'files/cache/macaddress.json')), 'r') as mac_json : data=json.load(mac_json)
                    autolog_color(typelog='info', text="Company > "+data["Company"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Address > "+data["Address"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    autolog_color(typelog='info', text="Block_Size > "+data["BlockSize"], wayinfo='%s' % (path_os(Config.system["Ways"]["info"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), nick=Config.user["NickName"], without_out_console=False)
                    match Config.system["Record Info in DataBase"]:
                        case "Yes" : _insert('%s' % (path_os(Config.system["DataBase"]["Way"]+Config.system["DataBase"]["Name"])), 'MAC', 
                                            data["Company"], 
                                            data["Address"], 
                                            data["BlockSize"])
                        case "No" : pass
                    cont=input('')
                case _ : raise Exceptions.NotFoundParameters("-> %s?" % (lang))
    def _help(lang):
        match lang:
            case "RUS":
                print("break_ip > пробить IP-Адрес")
                print("break_number > пробить номер телефона")
                print("break_mac > пробить MAC-Адрес")
                print("help > показать инструкции")
                print("clear > очистить окно")
                print("exit > выйти")
            case "ENG":
                print("break_ip > break IP-Address")
                print("break_number > break number phone")
                print("break_mac > break MAC-Address")
                print("help > show instructions")
                print("clear > clear window")
                print("exit > exit")

class Console:
    def __choice__(self, warn):
        match warn:
            case 1 : autolog_color(typelog='warning', text='Warn at call module "__choice__"', waywarn='%s' % (path_os(Config.system["Ways"]["warning"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])))
            case 0 : pass
        autolog_color(typelog='debug', text='Attempt - Completed!', waydebug='%s' % (path_os(Config.system["Ways"]["debug"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), without_out_console=True)
        while True:
            choice=input(f'{Config.user["NickName"]}{Config.user["ProgramName"]}> ')
            match choice:
                case "break_ip": 
                    autolog_color(typelog='debug', text='Trying call module "ip"', waydebug='%s' % (path_os(Config.system["Ways"]["debug"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), without_out_console=True)
                    Methods.ip(lang=Config.user["Language"])
                case "break_number": 
                    autolog_color(typelog='debug', text='Trying call module "number"', waydebug='%s' % (path_os(Config.system["Ways"]["debug"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), without_out_console=True)
                    Methods.number(lang=Config.user["Language"])
                case "break_mac": 
                    autolog_color(typelog='debug', text='Trying call module "mac"', waydebug='%s' % (path_os(Config.system["Ways"]["debug"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), without_out_console=True)
                    Methods.mac(lang=Config.user["Language"])
                case "help":
                    autolog_color(typelog='debug', text='Trying call module "help"', waydebug='%s' % (path_os(Config.system["Ways"]["debug"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), without_out_console=True)
                    Methods._help(lang=Config.user["Language"])
                case "exit" : quit()
                case "clear" : clear()
                case _ : print(f"Not found command -> {choice}")
    def __main__(self):
        match Config.system["Start Clear Window"]:
            case "Yes" : clear()
            case "No" : pass
            case _ : raise Exceptions.NotFoundParameters("-> %s?" % (Config.system["Start Clear Window"]))
        match Config.system["Start Show Banner"]:
            case "Yes":
                with open('%s' % (path_os(r'files/banner')), 'r') as banner : print(banner.read())
            case "No" : pass
            case _ : raise Exceptions.NotFoundParameters("-> %s?" % (Config.system["Start Show Banner"]))
        autolog_color(typelog='debug', text='Trying call module "__choice__"', waydebug='%s' % (path_os(Config.system["Ways"]["debug"])), waygeneral='%s' % (path_os(Config.system["Ways"]["general"])), without_out_console=True)
        try : self.__choice__(warn=0)
        except AttributeError : Console.__choice__(Any, warn=1)
