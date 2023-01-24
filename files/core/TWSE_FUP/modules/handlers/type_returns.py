class Type:
    from .exception import DataError, ParametersError
    import json
    def __init__(self, debug=True):
        self.debug=debug
    def __text__(self, name, *info, _answer):
        match name:
            case "break_ip":
                try:
                    datatextip = f"""
Continent        :::{info[0]}:::
Country          :::{info[1]}:::
Region           :::{info[2]}:::
City             :::{info[3]}:::
Lat              :::{info[4]}:::
Lon              :::{info[5]}:::
ISP              :::{info[6]}:::
ORG              :::{info[7]}:::
AS               :::{info[8]}:::
ASName           :::{info[9]}:::
Reverse          :::{info[10]}:::
MobileConnection :::{info[11]}:::
ProxyConnection  :::{info[12]}:::
Hosting          :::{info[13]}:::"""
                    data_frametextip = f"""
:::{info[0]}:::
:::{info[1]}:::
:::{info[2]}:::
:::{info[3]}:::
:::{info[4]}:::
:::{info[5]}:::
:::{info[6]}:::
:::{info[7]}:::
:::{info[8]}:::
:::{info[9]}:::
:::{info[10]}:::
:::{info[11]}:::
:::{info[12]}:::
:::{info[13]}:::"""
                except: raise self.DataError("Error work with data")
                finally:
                    match _answer:
                        case "text" : return data_frametextip
                        case "all" : return datatextip
                        case _ : raise self.ParametersError(f"Not found parameters -> {_answer}")
            case "break_number":
                try:
                    datatextnumber = f"""
Operator    :::{info[0]}:::
MNC         :::{info[1]}:::
Brand       :::{info[2]}:::
INN         :::{info[3]}:::
Work_Mobile :::{info[4]}:::
Name        :::{info[5]}:::
"""
                    data_frametextnumber = f"""
:::{info[0]}:::
:::{info[1]}:::
:::{info[2]}:::
:::{info[3]}:::
:::{info[4]}:::
:::{info[5]}:::
"""
                except: raise self.DataError("Error work with data")
                finally:
                    match _answer:
                        case "text" : return data_frametextnumber
                        case "all" : return datatextnumber
                        case _ : raise self.ParametersError(f"Not found parameters -> {_answer}")
            case "break_mac":
                try:
                    data = f"""
Company   :::{info[0]}:::
Address   :::{info[1]}:::
BlockSize :::{info[2]}:::
"""
                    data_frame = f"""
:::{info[0]}:::
:::{info[1]}:::
:::{info[2]}:::
"""
                except: raise self.DataError("Error work with data")
                finally:
                    match _answer:
                        case "text" : return data_frame
                        case "all" : return data
                        case _ : raise self.ParametersError(f"Not found parameters -> {_answer}")
    def __json__(self, name, *info, path):
        match name:
            case "break_ip":
                try:
                    data_framejsonip = {
                        "Continent":f"{info[0]}",
                        "Country":f"{info[1]}",
                        "Region":f"{info[2]}",
                        "City":f"{info[3]}",
                        "Lat":f"{info[4]}",
                        "Lon":f"{info[5]}",
                        "ISP":f"{info[6]}",
                        "ORG":f"{info[7]}",
                        "AS":f"{info[8]}",
                        "ASName":f"{info[9]}",
                        "Reverse":f"{info[10]}",
                        "MobileConnection":f"{info[11]}",
                        "ProxyConnection":f"{info[12]}",
                        "Hosting":f"{info[13]}"
                    }
                except: raise self.DataError("Error work with data")
                finally:
                    with open(path, 'w', encoding='utf-8') as file : self.json.dump(data_framejsonip, file)
                    match self.debug:
                        case True :  print(data_framejsonip), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                        case False : pass
            case "break_number":
                try:
                    data_framejsonnumber = {
                        "Operator":f"{info[0]}",
                        "MNC":f"{info[1]}",
                        "Brand":f"{info[2]}",
                        "INN":f"{info[3]}",
                        "Work_Mobile":f"{info[4]}",
                        "Name":f"{info[5]}"
                    }
                except: raise self.DataError("Error work with data")
                finally:
                    with open(path, 'w', encoding='utf-8') as file : self.json.dump(data_framejsonnumber, file)
                    match self.debug:
                        case True : print(data_framejsonnumber), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                        case False : pass
            case "break_mac":
                try:
                    data_framejsonmac = {
                        "Company":f"{info[0]}",
                        "Address":f"{info[1]}",
                        "BlockSize":f"{info[2]}"
                    }
                except: raise self.DataError("Error work with data")
                finally:
                    with open(path, 'w', encoding='utf-8') as file : self.json.dump(data_framejsonmac, file)
                    match self.debug:
                        case True : print(data_framejsonmac), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                        case False : pass
    def __file__(self, name, *info, path, view="ini", _mode="w"):
        match name:
            case "break_ip":
                match view:
                    case "ini":
                        try:
                            datainiip = f"""
[IP]
Continent={info[0]}
Country={info[1]}
Region={info[2]}
City={info[3]}
Lat={info[4]}
Lon={info[5]}
ISP={info[6]}
ORG={info[7]}
AS={info[8]}
ASName={info[9]}
Reverse={info[10]}
MobileConnection={info[11]}
ProxyConnection={info[12]}
Hosting={info[13]}"""
                        except: raise self.DataError("Error work with data")
                        finally:
                            with open(path, mode=_mode, encoding='utf-8') as file : file.write(datainiip)
                            match self.debug:
                                case True : print(datainiip), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                                case False : pass
                    case "txt":
                        try:
                            datatxtip = f"""
{info[0]}
{info[1]}
{info[2]}
{info[3]}
{info[4]}
{info[5]}
{info[6]}
{info[7]}
{info[8]}
{info[9]}
{info[10]}
{info[11]}
{info[12]}
{info[13]}"""
                            print(datatxtip)
                        except: raise self.DataError("Error work with data")
                        finally:
                            with open(path, mode=_mode, encoding='utf-8') as file : file.write(datatxtip)
                            match self.debug:
                                case True : print(datatxtip), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                                case False : pass
                    case _ : self.ParametersError(f"Not found parameters -> {view}")
            case "break_number":
                match view:
                    case "ini":
                        try:
                            dataininumber = f"""
[NumberPhone]
Operator={info[0]}
MNC={info[1]}
Brand={info[2]}
INN={info[3]}
Work_Mobile={info[4]}
Name={info[5]}
"""
                        except: raise self.DataError("Error work with data")
                        finally:
                            with open(path, mode=_mode, encoding='utf-8') as file : file.write(dataininumber)
                            match self.debug:
                                case True : print(dataininumber), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                                case False : pass
                    case "txt":
                        try:
                            datatxtnumber = f"""
{info[0]}
{info[1]}
{info[2]}
{info[3]}
{info[4]}
{info[5]}
"""
                        except: raise self.DataError("Error work with data")
                        finally:
                            with open(path, mode=_mode, encoding='utf-8') as file : file.write(datatxtnumber)
                            match self.debug:
                                case True : print(datatxtnumber), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                                case False : pass
                    case _ : raise self.ParametersError(f"Not found parameters -> {view}")
            case "break_mac":
                match view:
                    case "ini":
                        try:
                            datainimac = f"""
[MAC]
Company={info[0]}
Address={info[1]}
BlockSize={info[3]}
"""
                        except: raise self.DataError("Error work with data")
                        finally:
                            with open(path, mode=_mode, encoding='utf-8') as file : file.write(datainimac)
                            match self.debug:
                                case True : print(datainimac), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                                case False : pass
                    case "txt":
                        try:
                            datatxtmac = f"""
{info[0]}
{info[1]}
{info[3]}
"""
                        except: raise self.DataError("Error work with data")
                        finally:
                            with open(path, mode=_mode, encoding='utf-8') as file : file.write(datatxtmac)
                            match self.debug:
                                case True : print(datatxtmac), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                                case False : pass
                    case _ : raise self.ParametersError(f"Not found parameters -> {view}")
    def __html__(self, name, *info, path):
        match name:
            case "break_ip":
                try:
                    datahtmlip = f"""<!DOCTYPE html>
<head>
    <title>TWSEConsoleFUP 0.3</title>
    <meta charset="utf-8">
</head>
<body>
    <div class="Continent">{info[0]}
    </div>
    <div class="Country">{info[1]}
    </div>
    <div class="RegionName">{info[2]}
    </div>
    <div class="City">{info[3]}
    </div>
    <div class="Lat">{info[4]}
    </div>
    <div class="Lon">{info[5]}
    </div>
    <div class="ISP">{info[6]}
    </div>
    <div class="ORG">{info[7]}
    </div>
    <div class="AS">{info[8]}
    </div>
    <div class="ASName">{info[9]}
    </div>
    <div class="Reverse">{info[10]}
    </div>
    <div class="MobileConnection">{info[11]}
    </div>
    <div class="ProxyConnection">{info[12]}
    </div>
    <div class="Hosting">{info[13]}
    </div>
</body>
"""
                except: raise self.DataError("Error work with data")
                finally:
                        with open(path, mode='w', encoding='utf-8') as file : file.write(datahtmlip)
                        match self.debug:
                            case True : print(datahtmlip), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                            case False : pass
            case "break_number":
                try:
                    datahtmlnumber = f"""<!DOCTYPE html>
<head>
    <title>TWSEConsoleFUP 0.3</title>
    <meta charset="utf-8">
</head>
<body>
    <div class="OperName">{info[0]}
    </div>
    <div class="MNC">{info[1]}
    </div>
    <div class="Brand">{info[2]}
    </div>
    <div class="INN">{info[3]}
    </div>
    <div class="Work_Mobile">{info[4]}
    </div>
    <div class="Name">{info[5]}
    </div>
</body>
"""
                except: raise self.DataError("Error work with data")
                finally:
                        with open(path, mode='w', encoding='utf-8') as file : file.write(datahtmlnumber)
                        match self.debug:
                            case True : print(datahtmlnumber), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                            case False : pass
            case "break_mac":
                try:
                    datahtmlmac = f"""<!DOCTYPE html>
<head>
    <title>TWSEConsoleFUP 0.3</title>
    <meta charset="utf-8">
</head>
<body>
    <div class="Company">{info[0]}
    </div>
    <div class="Address">{info[1]}
    </div>
    <div class="BlockSize">{info[2]}
    </div>
</body>
"""
                except: raise self.DataError("Error work with data")
                finally:
                        with open(path, mode='w', encoding='utf-8') as file : file.write(datahtmlmac)
                        match self.debug:
                            case True : print(datahtmlmac), print('[ TWSE_FUP ] - [ Code returned "True" ]')
                            case False : pass