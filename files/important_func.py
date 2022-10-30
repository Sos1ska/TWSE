import os, sys, zipfile
try:
    from LOGer import autolog_color
except ImportError:
    from .core import autolog_color

def load_pyc_files(filepath):
    path, fname = os.path.split(filepath)
    module, _ = os.path.splitext(fname)
        
    if path not in sys.path:            
        sys.path.insert(0, path)
        
    return __import__(module)

def unzip_config(record):
    if record == True:
        autolog_color(typelog='debug', text='Starting Work module-{unzip_config}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
        try:
            with zipfile.ZipFile(r'files\buffer\system.zip') as archive:
                archive.extractall(r'files\config')
            with zipfile.ZipFile(r'files\buffer\color.zip') as archive3:
                archive3.extractall(r'files\config')
        except FileNotFoundError:
            autolog_color(typelog='error', text='Not Found File with type "zip"', typemsg='Message', wayerror=r'files\log\error.log', waygeneral=r'files\log\general.log', without_out_console=False)
            quit()
        autolog_color(typelog='debug', text='Unzip file module-{unzip_config}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
        autolog_color(typelog='debug', text='Exit module-{unzip_config}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
    elif record == False:
        with zipfile.ZipFile(r'files\buffer\system.zip') as archive2:
            archive2.extractall(r'files\config')
        with zipfile.ZipFile(r'files\buffer\color.zip') as archive4:
                archive4.extractall(r'files\config')

def delete_config(record):
    files = ['system.json', 'color.json']
    if record == True:
        autolog_color(typelog='debug', text='Starting Work module-{delete_config}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
        for file in files:
            os.remove(r'files\config\%s' % (file))
        autolog_color(typelog='debug', text='Delete files module-{delete_config}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
        autolog_color(typelog='debug', text='Exit module-{delete_config}', typemsg='Message', waydebug=r'files\log\debug.log', waygeneral=r'files\log\general.log', without_out_console=False)
    elif record == False:
        for file in files:
            os.remove(r'files\config\%s' % (file))

def create_buffer():
    os.mkdir(r'files\buffer')
