my_name_file = "break_ip"
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
    def __file__(self, continent, country, regionname, city, lat, lon, isp, org, asb, asname, reverse, mobile, proxy, hosting):
        data_for_out = f"""[{str(datetime.datetime.now().date())}]
Continent={continent}
Country={country}
RegionName={regionname}
City={city}
Lat={lat}
Lon={lon}
ISP={isp}
ORG={org}
AS={asb}
ASName={asname}
Reverse={reverse}
MobileConnection={mobile}
ConnectionProxy={proxy}
Hosting={hosting}"""
        return data_for_out
    def __text__(self, continent, country, regionname, city, lat, lon, isp, org, asb, asname, reverse, mobile, proxy, hosting):
        data_for_out = f"""
\t\t\tContinent         :::{continent}:::\n
\t\t\tCountry           :::{country}:::\n
\t\t\tRegionName        :::{regionname}:::\n
\t\t\tCity              :::{city}:::\n
\t\t\tLat               :::{lat}:::\n
\t\t\tLon               :::{lon}:::\n
\t\t\tISP               :::{isp}:::\n
\t\t\tORG               :::{org}:::\n
\t\t\tAS                :::{asb}:::\n
\t\t\tASName            :::{asname}:::\n
\t\t\tReverse           :::{reverse}:::\n
\t\t\tMobileConnection  :::{mobile}:::\n
\t\t\tConnectionProxy   :::{proxy}:::\n
\t\t\tHosting           :::{hosting}:::\n"""
        return data_for_out
    def __html__(self, continent, country, regionname, city, lat, lon, isp, org, asb, asname, reverse, mobile, proxy, hosting):
        html = f"""<!DOCTYPE html>
<head>
    <title>TWSEConsoleFUP 0.2</title>
</head>
<body>
    <div class="Continent">{continent}
    </div>
    <div class="Country">{country}
    </div>
    <div class="RegionName">{regionname}
    </div>
    <div class="City">{city}
    </div>
    <div class="Lat">{lat}
    </div>
    <div class="Lon">{lon}
    </div>
    <div class="ISP">{isp}
    </div>
    <div class="ORG">{org}
    </div>
    <div class="AS">{asb}
    </div>
    <div class="ASName">{asname}
    </div>
    <div class="Reverse">{reverse}
    </div>
    <div class="MobileConnection">{mobile}
    </div>
    <div class="ProxyConnection">{proxy}
    </div>
    <div class="Hosting">{hosting}
    </div>
</body>
"""
        return html
    def __json__(self, continent, country, regionname, city, lat, lon, isp, org, asb, asname, reverse, mobile, proxy, hosting):
        jsona = {
            "Continent": f"{continent}",
            "Country": f"{country}",
            "RegionName": f"{regionname}",
            "City": f"{city}",
            "Lat": f"{lat}",
            "Lon": f"{lon}",
            "ISP": f"{isp}",
            "ORG": f"{org}",
            "AS": f"{asb}",
            "ASName": f"{asname}",
            "Reverse": f"{reverse}",
            "MobileConnection": f"{mobile}",
            "ProxyConnection": f"{proxy}",
            "Hosting": f"{hosting}"
        }
        return jsona
    def __excel__(self, continent, country, regionname, city, lat, lon, isp, org, asb, asname, reverse, mobile, proxy, hosting):
        DataFrames = DataFrame({"Continent" : [continent],
                                "Country" : [country],
                                "RegionName" : [regionname],
                                "City" : [city],
                                "Lat" : [lat],
                                "Lon" : [lon],
                                "ISP" : [isp],
                                "ORG" : [org],
                                "AS" : [asb],
                                "ASName" : [asname],
                                "Reverse" : [reverse],
                                "MobileConnection" : [mobile],
                                "ProxyConnection" : [proxy],
                                "Hosting" : [hosting]})
        return DataFrames

class BreakIPAddress(Constructor):
    my_name_class = "BreakIPAddress"

    way = ""
    mode = ""
    ip = ""
    autoprint = ""
    debug = ""

    modelist = ["FileAnswer", "OnlyText", "HTML", "JSON", "EXCEL"]
    speclist = ["FileAnswer", "HTML", "JSON", "EXCEL"]

    def __init__(self, mode, ip=bytes, way=None, autoprint=True or False, debug=True or False):
        """`mode` - Sets the mode for the answer.
        There are 4 in total -> "FileAnswer", "OnlyText", "HTML", "JSON", "EXCEL".
        
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
        self.ip=ip
        self.autoprint=autoprint
        self.debug=debug
        if mode in self.modelist:
            if mode in self.speclist:
                if way == None or way == "" or way == " " : raise Base(f'[ {my_name_file}.{self.my_name_class} ] - [ Way ust be mandatory for "FileAnswer", "HTML", "JSON", "EXCEL"! Your mode -> {mode} ]')
                else : self.way=way
        else : raise NotFoundParameters(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found Parameters -> {mode} ]')

    def main(self):
        if self.mode == "OnlyText":
            send_requests = get(f'http://ip-api.com/json/{self.ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            if self.autoprint == True or self.autoprint == "True" : print(
                super().__text__(Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], Handler["lat"], Handler["lon"], Handler["isp"], Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"])
            )
            elif self.autoprint == False or self.autoprint == "False" : return super().__text__(Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], Handler["lat"], Handler["lon"], Handler["isp"], Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"])
            else : raise NotFoundParameters(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found Parameters -> {self.autoprint} ]')
        elif self.mode == "FileAnswer":
            send_requests = get(f'http://ip-api.com/json/{self.ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            try:
                with open(self.way, "w+", encoding='utf-8') as file : file.write(super().__file__(Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], Handler["lat"], Handler["lon"], Handler["isp"], Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"])), file.close()
            except FileNotFoundError : raise FileErrorTWSE(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found path, maybe your folder delete -> {self.way} ]')
            if self.debug == True or self.debug == "True":
                print(f'[ {my_name_file}.{self.my_name_class} ] - [ Code returned "1" ]')
        elif self.mode == "HTML":
            send_requests = get(f'http://ip-api.com/json/{self.ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            try:
                with open(self.way, "w+", encoding='utf-8') as file : file.write(super().__html__(Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], Handler["lat"], Handler["lon"], Handler["isp"], Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"])), file.close()
            except FileNotFoundError : raise FileErrorTWSE(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found path, maybe your folder delete -> {self.way} ]')
            if self.debug == True or self.debug == "True":
                print(f'[ {my_name_file}.{self.my_name_class} ] - [ Code returned "1" ]')
        elif self.mode == "JSON":
            send_requests = get(f'http://ip-api.com/json/{self.ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            try:
                with open(self.way, "w", encoding='utf-8') as file : dump(super().__json__(Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], Handler["lat"], Handler["lon"], Handler["isp"], Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"]), file), file.close()
            except FileNotFoundError : raise FileErrorTWSE(f'[ {my_name_file}.{self.my_name_class} ] - [ Not Found path, maybe your folder delete -> {self.way} ]')
            if self.debug == True or self.debug == "True":
                print(f'[ {my_name_file}.{self.my_name_class} ] - [ Code returned "1" ]')
        elif self.mode == "EXCEL":
            if os.path.isfile(self.way) == False : mode = 'w'
            else : mode = 'a'
            send_requests = get(f'http://ip-api.com/json/{self.ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting')
            answer = send_requests
            soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            Data = super().__excel__(Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], Handler["lat"], Handler["lon"], Handler["isp"], Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"])
            with ExcelWriter(self.way, engine="openpyxl", mode=mode) as writer : Data.to_excel(writer, sheet_name="IP")
            if self.debug == True or self.debug == "True":
                print(f'[ {my_name_file}.{self.my_name_class} ] - [ Code returned "1" ]')