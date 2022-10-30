import io, zipfile
from json import load, loads, dump, dumps
from .important_func import load_pyc_files
try:
    from LOGer import autolog_color
except ImportError:
    from .core import autolog_color

def CreateSYSconfig(record):
    if record == True:
        autolog_color(typelog='debug', text='Starting Work module-{CreateSYSconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
        ram=io.BytesIO()
        structure=load_pyc_files(r'files\structure_config.pyc')
        autolog_color(typelog='debug', text='Import pyc file module-{CreateSYSconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
        with zipfile.ZipFile(ram, 'w') as fileinram:
            autolog_color(typelog='debug', text='Create file in ram module-{CreateSYSconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
            with io.BytesIO() as json_ram:
                data=dumps(structure.systemC())
                autolog_color(typelog='debug', text='Read data pyc file module-{CreateSYSconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
                json_ram.write(data.encode())
                autolog_color(typelog='debug', text='Record in file module-{CreateSYSconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
                json_ram.seek(0)

                fileinram.writestr('system.json', json_ram.read())
        with open(r'files\buffer\system.zip', 'wb') as file:
            autolog_color(typelog='debug', text='Create zip file module-{CreateSYSconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
            ram.seek(0)
            file.write(ram.read())
        autolog_color(typelog='debug', text='Read ram and record in zip file module-{CreateSYSconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
    elif record == False:
        ram=io.BytesIO()
        structure=load_pyc_files(r'files\structure_cofnig.pyc')
        with zipfile.ZipFile(ram, 'w') as fileinram:
            with io.BytesIO() as json_ram:
                data=dumps(structure.systemC())
                json_ram.write(data.encode())
                json_ram.seek(0)
            
                fileinram.writestr('system.json', json_ram.read())
        with open(r'files\buffer\system.zip', 'wb') as file:
            ram.seek(0)
            file.write(ram.read())

def CreateCOLORconfig(record):
    if record == True:
        autolog_color(typelog='debug', text='Starting Work module-{CreateCOLORconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
        ram=io.BytesIO()
        structure=load_pyc_files(r'files\structure_config.pyc')
        autolog_color(typelog='debug', text='Import pyc file module-{CreateCOLORconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
        with zipfile.ZipFile(ram, 'w') as fileinram:
            autolog_color(typelog='debug', text='Create file in ram module-{CreateCOLORconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
            with io.BytesIO() as json_ram:
                data=dumps(structure.color())
                autolog_color(typelog='debug', text='Read data pyc file module-{CreateCOLORconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
                json_ram.write(data.encode())
                autolog_color(typelog='debug', text='Record in file module-{CreateCOLORconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
                json_ram.seek(0)

                fileinram.writestr('color.json', json_ram.read())
        with open(r'files\buffer\color.zip', 'wb') as file:
            autolog_color(typelog='debug', text='Create zip file module-{CreateCOLORconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
            ram.seek(0)
            file.write(ram.read())
        autolog_color(typelog='debug', text='Read ram and record in zip file module-{CreateCOLORconfig}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
    elif record == False:
        ram=io.BytesIO()
        structure=load_pyc_files(r'files\structure_config.pyc')
        with zipfile.ZipFile(ram, 'w') as fileinram:
            with io.BytesIO() as json_ram:
                data=dumps(structure.color())
                json_ram.write(data.encode())
                json_ram.seek(0)

                fileinram.writestr('color.json', json_ram.read())
        with open(r'files\buffer\color.zip', 'wb') as file:
            ram.seek(0)
            file.write(ram.read())
