__author__ = '\nSos1ska\nhttps://github.com/Sos1ska\nhttps://vk.com/nikitasos1ska'
__code__ = '\n\nOpenSourceCode'

try:
    from LOGer import autolog_color, _error_color, _warning_color, _info_color
except ImportError:
    print('[ TWSEConsole ] - [ Install lib "LOGer" ]')
try:
    from TWSE_FUP import BreakIPAddress, BreakMACAddress, BreakNumberPhone
except ImportError:
    _error_color("str", "Install lib \"TWSE_FUP\"", "TWSEConsole", TypeError="CRITICAL", WriteTime=True)

try:
    from .important_func import *
except ImportError:
    _error_color("str", "Damaged local packages!", "TWSEConsole", TypeError="CRITICAL", WriteTime=True)
try:
    from .debug import _debug
except ImportError:
    _error_color("str", "Damaged local packages!", "TWSEConsole", TypeError="CRITICAL", WriteTime=True)
try:
    from .record_database import _insert
except ImportError:
    _error_color("str", "Damaged local packages!", "TWSEConsole", TypeError="CRITICAL", WriteTime=True)
try:
    from .create_database import _create
except ImportError:
    _error_color("str", "Damaged local packages!", "TWSEConsole", TypeError="CRITICAL", WriteTime=True)

from .core.generation_proxy import Generate
from .ccf import CreateSYSconfig, CreateUSERconfig

from json import load, loads

# Очистка консоли
def clear():
    import os
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

# Проверка работоспособности proxy
def __proxy__(check_=None):
    import os
    from bs4 import BeautifulSoup
    from requests import get, exceptions
    match check_:
        case None:
            match os.path.exists(path_os(r"files/config/proxy.json")):
                case True:
                    with open(r'files/config/proxy.json', 'r') as file_proxy : proxy = load(file_proxy)
                    send_request = get("http://ip-api.com/json")
                    answer = send_request
                    soup_json = BeautifulSoup(answer.text, "html.parser").text.strip()
                    site_json = loads(soup_json)
                    Handler = site_json
                    user_ip = Handler["query"]
                    try:
                        send_request_proxy = get("http://ip-api.com/json", proxies=proxy)
                    except exceptions.ConnectionError:
                        _error_color(View='str', TEXT='Not Found connection to internet', NickName='TWSE_root_proxy', WriteTime=True)
                        quit()
                    answer_proxy = send_request_proxy
                    soup_json_proxy = BeautifulSoup(answer_proxy.text, "html.parser").text.strip()
                    site_json_proxy = loads(soup_json_proxy)
                    Handler_proxy = site_json_proxy
                    user_ip_proxy = Handler_proxy["query"]
                    if user_ip == user_ip_proxy:
                        _warning_color(View='str', TEXT='Proxy not working', NickName='TWSE_root_proxy', WriteTime=True)
                        return None
                    else:
                        return proxy
                case False:
                    pass
        case _:
            with open(r'files/config/proxy.json', 'r') as file_proxy : proxy = load(file_proxy)
            send_request = get("http://ip-api.com/json")
            answer = send_request
            soup_json = BeautifulSoup(answer.text, "html.parser").text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            user_ip = Handler["query"]
            try:
                send_request_proxy = get("http://ip-api.com/json", proxies=proxy)
            except exceptions.ConnectionError:
                _error_color(View='str', TEXT='Not Found connection to internet', NickName='TWSE_root_proxy', WriteTime=True)
                quit()
            answer_proxy = send_request_proxy
            soup_json_proxy = BeautifulSoup(answer_proxy.text, "html.parser").text.strip()
            site_json_proxy = loads(soup_json_proxy)
            Handler_proxy = site_json_proxy
            user_ip_proxy = Handler_proxy["query"]
            if user_ip == user_ip_proxy:
                _warning_color(View='str', TEXT='Proxy not working', NickName='TWSE_root_proxy', WriteTime=True)
                return False
            else:
                return True

def logging(text, typelog, _out=_debug):
    match _out:
        case True:
            system_config = _config.system_config
            info = system_config["Ways"]["info"]
            error = system_config["Ways"]["error"]
            debug = system_config["Ways"]["debug"]
            warning = system_config["Ways"]["warning"]
            general = system_config["Ways"]["general"]
            autolog_color(typelog, text, "{DM}", error, debug, warning, info, general, nick=_config.user_config["NickName"], without_out_console=False)
        case False : pass

def __scan__(host, port):
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        connect = sock.connect((host, port))
        _info_color("str", f"Port {port} : open", _config.user_config["NickName"], False)
        sock.close()
    except : pass

# Загрузка настроек
class _config:
    with open(path_os('files/config/user.json'), 'r') as user_file : user_config = load(user_file)
    with open(path_os('files/config/system.json'), 'r') as system_file : system_config = load(system_file) 

# Методы работы программы в консоли
class _methods(_config):
    __name__=__qualname__
    def __init__(self):
        logging(text=f"Starting work {__name__}.{self.__name__}", typelog="debug")
        self.user_config = super().user_config
        self.system_config = super().system_config
        while True:
            choice = input(self.user_config["NickName"] + self.user_config["ProgramName"] + '> ')
            match choice:
                case "break_ip" : self.ip()
                case "help" : self.help()
                case "break_mac" : self.mac()
                case "break_number" : self.number()
                case "create_db" : self.create_db()
                case "generate_proxy" : self.generation_proxy()
                case "reconfig" : self.reconfig()
                case "scan_port" : self.scan_port()
                case "clear" : clear()
                case "exit":
                    logging(text="Exit", typelog="info")
                    quit()
                case _:
                    _error_color(View="str", TEXT=f"Unknown command -> %s" % (choice), NickName=self.user_config["NickName"], WriteTime=True)

    # Метод ip 
    def ip(self):
        match self.system_config["Start Clear Window"]:
            case "Yes" : clear()
            case "No" : pass
        logging(text=f"Starting work \"ip\"", typelog="debug")
        match self.user_config["Language"]:
            case "RUS":
                print('Введите IP-Адрес')
                ip = input('> ')    
                BreakIPAddress(mode="OnlyText", ip=ip, autoprint=True, proxy=__proxy__()).main(_answer="all")
                match self.system_config["Record Info in DataBase"]:
                    case "Yes":
                        BreakIPAddress(mode="JSON", ip=ip, way=path_os(r'files/cache/ip.json'), debug=True, proxy=__proxy__()).main(_mode="w")
                        with open(r'files/cache/ip.json', 'r') as ip_json : data_ip = load(ip_json)
                        _insert(self.system_config["DataBase"]["Way"]+self.system_config["DataBase"]["Name"], "IP", data_ip["Continent"], data_ip["Country"], data_ip["Region"], data_ip["City"], data_ip["Lat"], data_ip["Lon"], data_ip["ISP"], data_ip["ORG"], data_ip["AS"], data_ip["ASName"], data_ip["Reverse"], data_ip["MobileConnection"], data_ip["ProxyConnection"], data_ip["Hosting"])
                    case "No" : pass
            case "ENG":
                print('Enter IP-Address')
                ip = input('> ')    
                BreakIPAddress(mode="OnlyText", ip=ip, autoprint=True, proxy=__proxy__()).main(_answer="all")
                match self.system_config["Record Info in DataBase"]:
                    case "Yes":
                        BreakIPAddress(mode="JSON", ip=ip, way=path_os(r'files/cache/ip.json'), debug=True, proxy=__proxy__()).main(_mode="w")
                        with open(r'files/cache/ip.json', 'r') as ip_json : data_ip = load(ip_json)
                        _insert(self.system_config["DataBase"]["Way"]+self.system_config["DataBase"]["Name"], "IP", data_ip["Continent"], data_ip["Country"], data_ip["Region"], data_ip["City"], data_ip["Lat"], data_ip["Lon"], data_ip["ISP"], data_ip["ORG"], data_ip["AS"], data_ip["ASName"], data_ip["Reverse"], data_ip["MobileConnection"], data_ip["ProxyConnection"], data_ip["Hosting"])
                    case "No" : pass
            case _:
                _error_color(View="str", TEXT=f"Not found parameters -> %s" % (self.user_config["Language"]), NickName=self.user_config["NickName"], WriteTime=True)
                logging(text=f"The end work \"ip\" with error", typelog="error")

        logging(text=f"The end work \"ip\"", typelog="debug")

    # Метод mac
    def mac(self):
        match self.system_config["Start Clear Window"]:
            case "Yes" : clear()
            case "No" : pass
        logging(text="Starting work \"mac\"", typelog="debug")
        match self.user_config["Language"]:
            case "RUS":
                print('Введите MAC-Адрес')
                mac = input('> ')    
                BreakMACAddress(mode="OnlyText", mac=mac, autoprint=True, proxy=__proxy__()).main(_answer="all")
                match self.system_config["Record Info in DataBase"]:
                    case "Yes":
                        BreakMACAddress(mode="JSON", mac=mac, way=path_os(r'files/cache/mac.json'), debug=True, proxy=__proxy__()).main(_mode="w")
                        with open(r'files/cache/mac.json', 'r') as mac_json : data_mac = load(mac_json)
                        _insert(self.system_config["DataBase"]["Way"]+self.system_config["DataBase"]["Name"], "MAC", data_mac["Company"], data_mac["Address"], data_mac["BlockSize"])
                    case "No" : pass
            case "ENG":
                print('Enter MAC-Address')
                mac = input('> ')    
                BreakMACAddress(mode="OnlyText", mac=mac, autoprint=True, proxy=__proxy__()).main(_answer="all")
                match self.system_config["Record Info in DataBase"]:
                    case "Yes":
                        BreakMACAddress(mode="JSON", mac=mac, way=path_os(r'files/cache/mac.json'), debug=True, proxy=__proxy__()).main(_mode="w")
                        with open(r'files/cache/mac.json', 'r') as mac_json : data_mac = load(mac_json)
                        _insert(self.system_config["DataBase"]["Way"]+self.system_config["DataBase"]["Name"], "MAC", data_mac["Company"], data_mac["Address"], data_mac["BlockSize"])
                    case "No" : pass
            case _:
                _error_color(View="str", TEXT=f"Not found parameters -> %s" % (self.user_config["Language"]), NickName=self.user_config["NickName"], WriteTime=True)
                logging(text=f"The end work \"mac\" with error", typelog="error")
        logging(text="The end work \"mac\"")

    # Метод number
    def number(self):
        match self.system_config["Start Clear Window"]:
            case "Yes" : clear()
            case "No" : pass
        logging(text="Starting work \"number\"", typelog="debug")
        match self.user_config["Language"]:
            case "RUS":
                print('Введите Номер телефона')
                number = input('> ')    
                BreakNumberPhone(mode="OnlyText", number=number, autoprint=True, proxy=__proxy__()).main(_answer="all")
                match self.system_config["Record Info in DataBase"]:
                    case "Yes":
                        BreakNumberPhone(mode="JSON", number=number, way=path_os(r'files/cache/number.json'), debug=True, proxy=__proxy__()).main(_mode="w")
                        with open(r'files/cache/mac.json', 'r') as mac_json : data_mac = load(mac_json)
                        _insert(self.system_config["DataBase"]["Way"]+self.system_config["DataBase"]["Name"], "MAC", data_mac["Company"], data_mac["Address"], data_mac["BlockSize"])
            case "ENG":
                print('Enter Number phone')
                number = input('> ')    
                BreakNumberPhone(mode="OnlyText", number=number, autoprint=True, proxy=__proxy__()).main(_answer="all")
                match self.system_config["Record Info in DataBase"]:
                    case "Yes":
                        BreakNumberPhone(mode="JSON", number=number, way=path_os(r'files/cache/number.json'), debug=True, proxy=__proxy__()).main(_mode="w")
                        with open(r'files/cache/mac.json', 'r') as number_json : data_number = load(number_json)
                        _insert(self.system_config["DataBase"]["Way"]+self.system_config["DataBase"]["Name"], "Number", data_number["Operator"], data_number["MNC"], data_number["Brand"], data_number["INN"], data_number["Work_Mobile"], data_number["Name"])
                    case "No" : pass
            case _:
                _error_color(View="str", TEXT=f"Not found parameters -> %s" % (self.user_config["Language"]), NickName=self.user_config["NickName"], WriteTime=True)
                logging(text=f"The end work \"number\" with error", typelog="error")
        logging(text="The end work \"number\"", typelog="debug")

    # Метод help
    def help(self):
        logging(text="Instruction out", typelog="debug")
        match self.user_config["Language"]:
            case "RUS":
                print('''break_ip -> Пробить IP-Адрес по api ip.com
break_mac -> Пробить MAC-Адрес по api 2ip.ua
break_number -> Пробить номер телефона по htmlweb.com
create_db -> Создать/пересоздать базу данных
generate_proxy -> Сгенерировать прокси сервер
reconfig -> Перенастроить файл с настройками
scan_port -> Сканировать на открытые порты
clear -> Очистить окно
exit -> Выход''')
            case "ENG":
                print('''break_ip -> Break IP-Address on api ip.com
break_mac -> Break MAC-Address on api 2ip.ua
break_number -> Break number phons on htmlweb.com
create_db -> Create/recreate data base
generate_proxy -> Generate proxy server
reconfig -> Reconfig file's with settings
scan_port -> Scan for open ports
clear -> Clear window
exit -> Exit''')

    # Метод создания базы данных
    def create_db(self):
        logging(text="Starting work \"create_db\"", typelog="debug")
        try:
            with open(self.system_config["DataBase"]["Way"]+self.system_config["DataBase"]["Name"], 'w') : pass
            _create(self.system_config["DataBase"]["Way"]+self.system_config["DataBase"]["Name"], self.system_config["Ways"]["error"], self.system_config["Ways"]["general"])
        except Exception as e:
            logging(text=e, typelog="error")
        finally:
            match self.user_config["Language"]:
                case "RUS" : logging(text="БазаДанных создана!", typelog="info")
                case "ENG" : logging(text="DataBase created!", typelog="info")
                case _:
                    logging(text=f"Not found parameters -> %s" % (self.user_config["Language"]), typelog="error")
                    logging(text=f"The end work \"create_db\" with error", typelog="error")
        logging(text="The end work \"create_db\"")

    # Метод генерации прокси сервера
    def generation_proxy(self):
        match self.system_config["Start Clear Window"]:
            case "Yes" : clear()
            case "No" : pass
        logging(text="Starting work \"generation_proxy\"", typelog="debug")
        match self.user_config["Language"]:
            case "RUS":
                Generate("RUS")
            case "ENG":
                Generate("ENG")
        with open(path_os(r'files/config/proxy.json'), 'r') as file_proxy : proxy = load(file_proxy)
        logging(text=str(proxy), typelog="info")
        logging(text="The end work \"generation_proxy\"", typelog="debug")
    
    # Метод пересоздания файлов настроек
    def reconfig(self):
        logging(text="Staring work \"reconfig\"", typelog="debug")
        CreateSYSconfig(record=True)
        CreateUSERconfig(record=True)
        unzip_config(record=True)
        match self.user_config["Language"]:
            case "RUS":
                logging(text="Перезапустите программу", typelog="info")
                quit()
            case "ENG":
                logging(text="Restart program", typelog="info")
                quit()
        logging(text="The end work \"reconfig\"", typelog="debug")

    # Метод сканирования портов
    def scan_port(self):
        import threading
        match self.system_config["Start Clear Window"]:
            case "Yes" : clear()
            case "No" : pass
        logging(text="Starting work \"scan_port\"", typelog="debug")
        host = input("host> ")
        for i in range(0, 10000):
            potoc = threading.Thread(target=__scan__, args=(host, i))
            potoc.start()
            potoc.join(0.5)
        logging(text="The end work \"scan_port\"", typelog="debug")

class _console:
    with open(path_os(r'files/banner'), 'r') as file_banner : print(file_banner.read())
    _methods()
