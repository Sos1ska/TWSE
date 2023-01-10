import io, zipfile
from json import load, loads, dump, dumps
from .important_func import load_pyc_files, path_os
try:
    from LOGer import autolog_color
except ImportError:
    from .core import autolog_color

def CreateSYSconfig(record):
    if record == True:
        autolog_color(typelog='debug', text='Starting Work module-{CreateSYSconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
        ram=io.BytesIO()
        structure=load_pyc_files('%s' % path_os(r'files/structure_config.py'))
        autolog_color(typelog='debug', text='Import pyc file module-{CreateSYSconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
        with zipfile.ZipFile(ram, 'w') as fileinram:
            autolog_color(typelog='debug', text='Create file in ram module-{CreateSYSconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
            with io.BytesIO() as json_ram:
                data=dumps(structure.systemC())
                autolog_color(typelog='debug', text='Read data pyc file module-{CreateSYSconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
                json_ram.write(data.encode())
                autolog_color(typelog='debug', text='Record in file module-{CreateSYSconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
                json_ram.seek(0)

                fileinram.writestr('system.json', json_ram.read())
        with open('%s' % path_os(r'files/cache/system.zip'), 'wb') as file:
            autolog_color(typelog='debug', text='Create zip file module-{CreateSYSconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
            ram.seek(0)
            file.write(ram.read())
        autolog_color(typelog='debug', text='Read ram and record in zip file module-{CreateSYSconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
    elif record == False:
        ram=io.BytesIO()
        structure=load_pyc_files('%s' % path_os(r'files/structure_config.py'))
        with zipfile.ZipFile(ram, 'w') as fileinram:
            with io.BytesIO() as json_ram:
                data=dumps(structure.systemC())
                json_ram.write(data.encode())
                json_ram.seek(0)
            
                fileinram.writestr('system.json', json_ram.read())
        with open('%s' % path_os(r'files/cache/system.zip'), 'wb') as file:
            ram.seek(0)
            file.write(ram.read())

def CreateUSERconfig(record):
    if record == True:
        autolog_color(typelog='debug', text='Starting Work module-{CreateUSERconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
        ram=io.BytesIO()
        structure=load_pyc_files('%s' % path_os(r'files/structure_config.py'))
        autolog_color(typelog='debug', text='Import pyc file module-{CreateUSERconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
        with zipfile.ZipFile(ram, 'w') as fileinram:
            autolog_color(typelog='debug', text='Create file in ram module-{CreateUSERconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
            with io.BytesIO() as json_ram:
                data=dumps(structure.user())
                autolog_color(typelog='debug', text='Read data pyc file module-{CreateUSERconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
                json_ram.write(data.encode())
                autolog_color(typelog='debug', text='Record in file module-{CreateUSERconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
                json_ram.seek(0)

                fileinram.writestr('user.json', json_ram.read())
        with open('%s' % path_os(r'files/cache/user.zip'), 'wb') as file:
            autolog_color(typelog='debug', text='Create zip file module-{CreateUSERconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
            ram.seek(0)
            file.write(ram.read())
        autolog_color(typelog='debug', text='Read ram and record in zip file module-{CreateUSERconfig}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
    elif record == False:
        ram=io.BytesIO()
        structure=load_pyc_files('%s' % path_os(r'files/structure_config.py'))
        with zipfile.ZipFile(ram, 'w') as fileinram:
            with io.BytesIO() as json_ram:
                data=dumps(structure.user())
                json_ram.write(data.encode())
                json_ram.seek(0)

                fileinram.writestr('user.json', json_ram.read())
        with open('%s' % path_os(r'files/cache/user.zip'), 'wb') as file:
            ram.seek(0)
            file.write(ram.read())
