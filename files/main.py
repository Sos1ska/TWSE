__author__ = '\nSos1ska\nhttps://github.com/Sos1ska\nhttps://vk.com/nikitasos1ska'
__code__ = '\n\nOpenSourceCode'

import os, sys
from important_func import load_pyc_files, unzip_config, delete_config
from ccf import CreateSYSConfig
from json import loads, load
from typing import Any

try:
    debugL=open(r'files\log\debug.log', 'a', encoding='utf-8')
except FileNotFoundError:
    debugL=open(r'DEBUG.log', 'w', encoding='utf-8')
try:
    errorL=open(r'files\log\error.log', 'a', encoding='utf-8')
except FileNotFoundError:
    errorL=open(r'ERROR.log', 'w', encoding='utf-8')
try:
    generalL=open(r'files\log\general.log', 'a', encoding='utf-8')
except FileNotFoundError:
    generalL=open(r'GENERAL.log', 'w', encoding='utf-8')

def clear():
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def _quit():
    debugL.close()
    errorL.close()
    generalL.close()
    delete_config()
    print('Exit')
    quit()

def open_again():
    try:
        debugL=open(r'files\log\debug.log', 'a', encoding='utf-8')
    except FileNotFoundError:
        debugL=open(r'DEBUG.log', 'w', encoding='utf-8')
    try:
        errorL=open(r'files\log\error.log', 'a', encoding='utf-8')
    except FileNotFoundError:
        errorL=open(r'ERROR.log', 'w', encoding='utf-8')
    try:
        generalL=open(r'files\log\general.log', 'a', encoding='utf-8')
    except FileNotFoundError:
        generalL=open(r'GENERAL.log', 'w', encoding='utf-8')

class methods:
    def _save_log(self=Any):
        debugL.close()
        errorL.close()
        generalL.close()
    from bs4 import BeautifulSoup
    log = load_pyc_files(r'log.pyc')
    def break_ip_mobile(self, systemC):
        from requests import get
        debugL.write(self.log.debug(View='txt', Text='Attempt - Compeleted!', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text='Attempt - Completed!', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        if systemC["ClearEveryTime"] == "No":
            pass
        elif systemC["ClearEveryTime"] == "Yes":
            clear()
        print('Break IP if he mobile')
        debugL.write(self.log.debug(View='txt', Text='Output next -> "Break IP if he mobile"', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text='Output next -> "Break IP if he mobile"', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        print('\nInsert IP-Address')
        debugL.write(self.log.debug(View='txt', Text='Output next -> "Insert IP-Address"', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text='Output next -> "Insert IP-Address"', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        ip=input('> ')
        send_request=get(f'https://htmlweb.ru/geo/api.php?ip={ip}&json')
        debugL.write(self.log.debug(View='txt', Text=f'Send request -> https://htmlweb.ru/geo/api.php?ip={ip}&json', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text=f'Send request -> https://htmlweb.ru/geo/api.php?ip={ip}&json', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        answer=send_request
        soup_json=self.BeautifulSoup(answer.text, 'html.parser').text.strip()
        debugL.write(self.log.debug(View='txt', Text='Get json', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Messsage', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text='Get json', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        site_json=loads(soup_json)
        debugL.write(self.log.debug(View='txt', Text='Read json answer', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text='Read json answer', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        Handler=site_json
        try:
            self.log.info(View='str', Text=Handler["country"]["name"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["county"]["name"], WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["county"]["name"], WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        except KeyError:
            self.log.info(View='str', Text='Not Found', WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        try:
            self.log.info(View='str', Text=Handler["country"]["iso"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["country"]["iso"], WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["country"]["iso"], WriteTime=True"', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        except KeyError:
            self.log.info(View='str', Text='Not Found', WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        try:
            self.log.info(View='str', Text=Handler["country"]["telcod"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["country"]["telcod"], WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["country"]["telcod"], WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        except KeyError:
            self.log.info(View='str', Text='Not Found', WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        try:
            self.log.info(View='str', Text=Handler["country"]["capital"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["country"]["capital"], WriteTime=True"', Sender=__name__+'.py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["country"]["capital"], WriteTime=True"', Sender=__name__+'py<class methods><break_ip_mobile>', TypeMSG='Message', WriteTime=True)+'\n')
        except KeyError:
            self.log.info(View='str', Text='Not Found', WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        try:
            self.log.info(View='str', Text=Handler["country"]["mcc"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=["country"]["mcc"], WriteTime=True"', Sender=__name__+'.py<class methods><break_ip_mobile>'))
        except KeyError:
            self.log.info(View='str', Text='Not Found', WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        self._save_log()
        cont=input('')
        open_again()
    def get_proxy(self, systemC):
        from requests import get
        debugL.write(self.log.debug(View='txt', Text='Attempt - Compeleted!', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text='Attempt - Completed!', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
        if systemC["ClearEveryTime"] == "No":
            pass
        elif systemC["ClearEveryTime"] == "Yes":
            clear()
        send_request=get('https://htmlweb.ru/json/proxy/get?country=RU&perpage=5')
        debugL.write(self.log.debug(View='txt', Text='Send request -> https://htmlweb.ru/json/proxy/get?country=RU&perpage=5', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text='Send request -> https://htmlweb.ru/json/proxy/get?country=RU&perpage=5', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
        answer=send_request
        soup_json=self.BeautifulSoup(answer.text, 'html.parser').text.strip()
        debugL.write(self.log.debug(View='txt', Text='Get json', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text='Get json', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
        site_json=loads(soup_json)
        debugL.write(self.log.debug(View='txt', Text='Read json answer', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text='Read json answer', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
        Handler=site_json
        try:
            self.log.info(View='str', Text=Handler["0"]["name"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["0"]["name"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["0"]["name"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            self.log.info(View='str', Text=Handler["0"]["type"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["0"]["type"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["0"]["type"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            self.log.info(View='str', Text=Handler["0"]["country"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["0"]["country"], WriteTime=True)"')+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["0"]["country"], WriteTime=True)"')+'\n')
        except KeyError:
            pass
        try:
            self.log.info(View='str', Text=Handler["1"]["name"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["1"]["name"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["1"]["name"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            self.log.info(View='str', Text=Handler["1"]["type"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["1"]["type"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["1"]["type"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            self.log.info(View='str', Text=Handler["1"]["country"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["1"]["country"], WriteTime=True)"')+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["1"]["country"], WriteTime=True)"')+'\n')
        except KeyError:
            pass
        try:
            self.log.info(View='str', Text=Handler["2"]["name"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["2"]["name"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["2"]["name"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            self.log.info(View='str', Text=Handler["2"]["type"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["2"]["type"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["2"]["type"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            self.log.info(View='str', Text=Handler["2"]["country"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["2"]["country"], WriteTime=True)"')+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["2"]["country"], WriteTime=True)"')+'\n')
        except KeyError:
            pass
        try:
            self.log.info(View='str', Text=Handler["3"]["name"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["3"]["name"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["3"]["name"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            self.log.info(View='str', Text=Handler["3"]["type"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["3"]["type"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["3"]["type"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            self.log.info(View='str', Text=Handler["3"]["country"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["3"]["country"], WriteTime=True)"')+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["3"]["country"], WriteTime=True)"')+'\n')
        except KeyError:
            pass
        try:
            self.log.info(View='str', Text=Handler["4"]["name"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["4"]["name"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["4"]["name"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            self.log.info(View='str', Text=Handler["4"]["type"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["4"]["type"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["4"]["type"], WriteTime=True)"', Sender=__name__+'.py<class methods><get_proxy>', TypeMSG='Message', WriteTime=True)+'\n')
            self.log.info(View='str', Text=Handler["4"]["country"], WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["4"]["country"], WriteTime=True)"')+'\n')
            generalL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["4"]["country"], WriteTime=True)"')+'\n')
        except KeyError:
            pass
        self._save_log()
        cont=input('')
        open_again()
    def break_ip_2ip(self, systemC):
        from requests import get
        debugL.write(self.log.debug(View='txt', Text='Attempt - Completed!', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text='Attempt - Completed!', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        if systemC["ClearEveryTime"] == "No":
            pass
        elif systemC["ClearEveryTime"] == "Yes":
            clear()
        print('Break IP use API 2IP')
        debugL.write(self.log.debug(View='txt', Text=f'Output next -> "Break IP use API 2IP"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text=f'Output next -> "Break IP use API 2IP"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        print('\nInsert IP-Address')
        debugL.write(self.log.debug(View='txt', Text=f'Output next -> "Insert IP-Address"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text=f'Output next -> "Insert IP-Address"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        ip=input('> ')
        send_request=get(f'https://api.2ip.ua/geo.json?ip={ip}')
        debugL.write(self.log.debug(View='txt', Text=f'Send request -> https://api.2ip.ua/geo.json?ip={ip}', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text=f'Send request -> https://api.2ip.ua/geo.json?ip={ip}', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        answer=send_request
        soup_json=self.BeautifulSoup(answer.text, 'html.parser').text.strip()
        debugL.write(self.log.debug(View='txt', Text=f'Get json', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text=f'Get json', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        site_json=loads(soup_json)
        debugL.write(self.log.debug(View='txt', Text=f'Read json answer', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text=f'Read json answer', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        Handler=site_json
        try:
            self.log.info(View='str', Text=Handler["country"], WriteTime=False)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["country"], WriteTime=False)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.info(View='txt', Text=Handler["country"], WriteTime=True)+'\n')
        except KeyError:
            self.log.info(View='str', Text='Not Found', WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.info(View='txt', Text='Not Found', WriteTime=True)+'\n')
        try:
            self.log.info(View='str', Text=Handler["region"], WriteTime=False)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["region"], WriteTime=False)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.info(View='txt', Text=Handler["region"], WriteTime=True)+'\n')
        except KeyError:
            self.log.info(View='str', Text='Not Found', WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.info(View='txt', Text='Not Found', WriteTime=True)+'\n')
        try:
            self.log.info(View='str', Text=Handler["city"], WriteTime=False)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=Handler["city"], WriteTime=False)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.info(View='txt', Text=Handler["city"], WriteTime=True)+'\n')
        except KeyError:
            self.log.info(View='str', Text='Not Found', WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.info(View='txt', Text='Not Found', WriteTime=True)+'\n')
        try:
            self.log.info(View='str', Text=Handler["latitude"]+' '+Handler["longitude"], WriteTime=False)
            debugL.write(self.log.debug(View='txt', Text=f'Use module "info(View=\'str\', Text=Handler["latitude"]+\' \'+Handler["longitude"], WriteTime=False)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
        except KeyError:
            self.log.info(View='str', Text='Not Found', WriteTime=True)
            debugL.write(self.log.debug(View='txt', Text='Use module "info(View=\'str\', Text=\'Not Found\', WriteTime=True)"', Sender=__name__+'.py<class methods><break_ip_2ip>', TypeMSG='Message', WriteTime=True)+'\n')
            generalL.write(self.log.info(View='txt', Text='Not Found', WriteTime=True)+'\n')
        self._save_log()
        cont=input('')
        open_again()

class _console(methods):
    log = load_pyc_files(r'log.pyc')
    with open(r'files\config\user.json') as file_user:
        data_user=load(file_user)
    def __choice__(self):
        debugL.write(self.log.debug(View='txt', Text=f'Attempt - Completed!', Sender=__name__+'.py<class _console><__choice__>', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text=f'Attempt - Completed!', Sender=__name__+'.py<class _console><__choice__>', TypeMSG='Message', WriteTime=True)+'\n')
        with open(r'files\config\system.json') as file_system:
            data=load(file_system)
        while True:
            choice=input(f'{self.data_user["UserName"]}{self.data_user["ProgramName"]}> ')
            if choice=="break_ip":
                super().break_ip_2ip(systemC=data)
            if choice=="get_proxy":
                super().get_proxy(systemC=data)
            if choice=="break_ip_mobile":
                super().break_ip_mobile(systemC=data)
            if choice=="exit":
                super()._save_log()
                _quit()
    def __main__(self):
        debugL.write(self.log.debug(View='txt', Text=f'Start file {__name__}.py', Sender=__name__+'.py', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text=f'Start file {__name__}.py', Sender=__name__+'.py', TypeMSG='Message', WriteTime=True)+'\n')
        CreateSYSConfig()
        unzip_config()
        debugL.write(self.log.debug(View='txt', Text=f'Start create "system.json"', Sender=__name__+'.py', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text=f'Start create "system.json"', Sender=__name__+'.py', TypeMSG='Meesage', WriteTime=True)+'\n')
        with open(r'files\config\system.json') as file_system:
            data=load(file_system)
        print(data["StartClearWindow"])
        if data["StartClearWindow"] == "Yes":
            clear()
        elif data["StartClearWindow"] == "No":
            pass
        if data["StartShowBanner"] == "Yes":
            try:
                with open(r'files\%s' % (self.data_user["LoadBanner"]["way1"]), 'r') as banner:
                    banner.seek(0)
                    print(banner.read())
                debugL.write(self.log.debug(View='txt', Text='Trying call "__choice__"', Sender=__name__+'.py', TypeMSG='Message', WriteTime=True)+'\n')
                generalL.write(self.log.debug(View='txt', Text='Trying call "__choice__"', Sender=__name__+'.py', TypeMSG='Message', WriteTime=True)+'\n')
                self.__choice__()
            except FileNotFoundError:
                generalL.write(self.log.warning(View='txt', Text='Not Found File -> %s' % (self.data_user["LoadBanner"]["way1"]), TypeMSG='Message', WriteTime=True)+'\n')
                try:
                    with open(r'files\%s' % (self.data_user["LoadBanner"]["way2"]), 'r') as banner:
                        banner.seek(0)
                        print(banner.read())
                    debugL.write(self.log.debug(View='txt', Text='Trying call "__choice__"', Sender=__name__+'.py', TypeMSG='Message', WriteTime=True)+'\n')
                    generalL.write(self.log.debug(View='txt', Text='Trying call "__choice__"', Sender=__name__+'.py', TypeMSG='Message', WriteTime=True)+'\n')
                    self.__choice__()
                except FileNotFoundError:
                    errorL.write(self.log.error(View='txt', Text='Not Found File -> %s' % (self.data_user["LoadBanner"]["way2"]), TypeMSG='Message', WriteTime=True)+'\n')
                    generalL.write(self.log.error(View='txt', Text='Not Found File -> %s' % (self.data_user["LoadBanner"]["way2"]), TypeMSG='Message', WriteTime=True)+'\n')
                    self.log.error(View='str', Text='Not Found File -> %s' % (self.data_user["LoadBanner"]["way2"]), TypeMSG='Message', WriteTime=True)
                    _quit()
        elif data["StartShowBanner"] == "No":
            pass
        debugL.write(self.log.debug(View='txt', Text='Trying call "__choice__"', Sender=__name__+'.py', TypeMSG='Message', WriteTime=True)+'\n')
        generalL.write(self.log.debug(View='txt', Text='Trying call "__choice__"', Sender=__name__+'.py', TypeMSG='Message', WriteTime=True)+'\n')
        self.__choice__()
