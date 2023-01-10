my_name_file = "break_mac"
import os

from ..Handlers.exceptions import ImportErrorTWSE, FileErrorTWSE, NotFoundParameters, Base

try : from requests import get
except ImportError : raise ImportErrorTWSE(f'[ {my_name_file} ] - [ Install lib "requests" ]')
try : from bs4 import BeautifulSoup
except ImportError : raise ImportErrorTWSE(f'[ {my_name_file} ] - [ Install lib "bs4" ]')
try : from pandas import *
except ImportError : raise ImportErrorTWSE(f'[ {my_name_file} ] - [ Install lib "pands" ]')

from json import loads, dump
import datetime

class Constructor:
    def __file__(self, company, address, block_size):
        data_for_out = f"""[{str(datetime.datetime.now().date())}]
Company={company}
Address={address}
BlockSize={block_size}
"""
        return data_for_out
    def __text__(self, company, address, block_size):
        data_for_out = f"""
\t\t\tCompany   :::{company}:::\n
\t\t\tAddress   :::{address}:::\n
\t\t\tBlockSize :::{block_size}:::\n"""
        return data_for_out
    def __html__(self, company, address, block_size):
        html = f"""<!DOCTYPE html>
<head>
    <title>TWSEConsoleFUP 0.1</title>
</head>
<body>
    <div class="Company">{company}
    </div>
    <div class="Address">{address}
    </div>
    <div class="BlockSize">{block_size}
    </div>
</body>
"""
        return html
    def __json__(self, company, address, block_size):
        jsona = {
            "Company": f"{company}",
            "Address": f"{address}",
            "BlockSize": f"{block_size}"
        }
        return jsona
    def __excel__(self, company, address, block_size):
        DataFrames = DataFrame({"Company" : [company],
                                "Address" : [address],
                                "Block_Size" : [block_size]})
        return DataFrames

class BreakMACAddress(Constructor):
    my_name_class = "BreakMACAddress"

    way = ""
    mode = ""
    mac = ""
    autoprint = ""
    debug = ""

    modelist = ["FileAnswer", "OnlyText", "HTML", "JSON", "EXCEL"]
    speclist = ["FileAnswer", "HTML", "JSON", "EXCEL"]

    def __init__(self, mode, mac=bytes, way=None, autoprint=True or False, debug=True or False):
        """`mode` - Sets the mode for the answer.
        There are 4 in total -> "FileAnswer", "OnlyText", "HTML", "JSON".
        
        `way` - Sets the path to a file and create him.
        There are 3 in total -> "FileAnswer", "HTML", "JSON".
        
        `autoprint` - Sets the auto print the answer.
        There are 1 in total -> "OnlyText".
        
        `debug` - Sets debug answer.
        There are 3 in total -> "FileAnswer", "HTML", "JSON".
        
        `FileAnswer` - Creates a file with a construction from a file with the ini extension, which allows it to be parsed if necessary.
        
        `OnlyText` - Outputs the answer as text. With autoprint allows you to automatically output to the console or transfer data.
        
        `HTML` - Creates a file with the html extension, will create a lighter one, because will allow it to be quickly parsed or simply output for the server.
        
        `JSON` - Creates a file with the json extension, will create an easier one, because will allow it to be quickly parsed or simply output for the server.
        
        `EXCEL` - Creates a file with the excel extension."""
        self.mode=mode
        self.mac=mac
        self.autoprint=autoprint
        self.debug=debug
        if mode in self.modelist:
            if mode in self.speclist:
                if way == None or way == "" or way == " " : raise Base(f'[ {my_name_file}.{self.my_name_class} ] - [ Way ust be mandatory for "FileAnswer", "HTML", "JSON"! Your mode -> {mode} ]')
                else : self.way=way
        else : raise NotFoundParameters(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found Parameters -> {mode} ]')

    def main(self):
        if self.mode == "OnlyText":
            send_requests = get(f'https://api.2ip.ua/mac.json?mac={self.mac}')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            if self.autoprint == True or self.autoprint == "True" : print(
                super().__text__(Handler["company"], Handler["address"], Handler["block_size"])
            )
            elif self.autoprint == False or self.autoprint == "False" : return super().__text__(Handler["company"], Handler["address"], Handler["block_size"])
            else : raise NotFoundParameters(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found Parameters -> {self.autoprint} ]')
        elif self.mode == "FileAnswer":
            send_requests = get(f'https://api.2ip.ua/mac.json?mac={self.mac}')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            try:
                with open(self.way, "w+", encoding='utf-8') as file : file.write(super().__file__(Handler["company"], Handler["address"], Handler["block_size"])), file.close()
            except FileNotFoundError : raise FileErrorTWSE(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found path, maybe your folder delete -> {self.way} ]')
            if self.debug == True or self.debug == "True":
                print(f'[ {my_name_file}.{self.my_name_class} ] - [ Code returned "1" ]')
        elif self.mode == "HTML":
            send_requests = get(f'https://api.2ip.ua/mac.json?mac={self.mac}')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            try:
                with open(self.way, "w+", encoding='utf-8') as file : file.write(super().__html__(Handler["company"], Handler["address"], Handler["block_size"])), file.close()
            except FileNotFoundError : raise FileErrorTWSE(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found path, maybe your folder delete -> {self.way} ]')
            if self.debug == True or self.debug == "True":
                print(f'[ {my_name_file}.{self.my_name_class} ] - [ Code returned "1" ]')
        elif self.mode == "JSON":
            send_requests = get(f'https://api.2ip.ua/mac.json?mac={self.mac}')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            try:
                with open(self.way, "w+", encoding='utf-8') as file : dump(super().__json__(Handler["company"], Handler["address"], Handler["block_size"]), file), file.close()
            except FileNotFoundError : raise FileErrorTWSE(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found path, maybe your folder delete -> {self.way} ]')
            if self.debug == True or self.debug == "True":
                print(f'[ {my_name_file}.{self.my_name_class} ] - [ Code returned "1" ]')
        elif self.mode == "EXCEL":
            if os.path.isfile(self.way) == False : mode = 'w'
            else : mode = 'a'
            send_requests = get(f'https://api.2ip.ua/mac.json?mac={self.mac}')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            Data = super().__excel__(Handler["companny"], Handler["address"], Handler["block_size"])
            with ExcelWriter(self.way, engine="openpyxl", mode=mode) as writer : Data.to_excel(writer, sheet_name="MAC")
            if self.debug == True or self.debug == "True":
                print(f'[ {my_name_file}.{self.my_name_class} ] - [ Code returned "1" ]')