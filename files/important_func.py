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

def path_os(way):
    if os.sys.platform == "win32":
        new_way=way.replace("/", "\\")
    else:
        new_way=way.replace("\\", "/")
    return new_way

def unzip_config(record):
    match record:
        case True:
            autolog_color(typelog='debug', text='Starting Work module-{unzip_config}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
            try:
                with zipfile.ZipFile('%s' % (path_os(r'files/cache/system.zip'))) as archive : archive.extractall('%s' % (path_os(r'files/config')))
                with zipfile.ZipFile('%s' % (path_os(r'files/cache/color.zip'))) as archive3 : archive3.extractall('%s' % (path_os(r'files/config')))
                with zipfile.ZipFile('%s' % (path_os(r'files/cache/user.zip'))) as archive5 : archive5.extractall('%s' % (path_os(r'files/config')))
            except FileNotFoundError:
                autolog_color(typelog='error', text='Not Found File with type "zip"', typemsg='Message', wayerror=r'files\log\error.log', waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
                quit()
            autolog_color(typelog='debug', text='Unzip file module-{unzip_config}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
            autolog_color(typelog='debug', text='Exit module-{unzip_config}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
        case False:
            with zipfile.ZipFile('%s' % (path_os(r'files/cache/system.zip'))) as archive2 : archive2.extractall('%s' % (path_os(r'files/config')))
            with zipfile.ZipFile('%s' % (path_os(r'files/cache/color.zip'))) as archive4 : archive4.extractall('%s' % (path_os(r'files/config')))
            with zipfile.ZipFile('%s' % (path_os(r'files/cache/user.zip'))) as archive6 : archive6.extractall('%s' % (path_os(r'files/config')))

def delete_config(record):
    files = ['system.json', 'color.json', 'user.json']
    match record:
        case True:
            autolog_color(typelog='debug', text='Starting Work module-{delete_config}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
            for file in files : os.remove('%s' % (
                                                 path_os(r'files/config/%s' % (file))
                                                ))
            autolog_color(typelog='debug', text='Delete files module-{delete_config}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
            autolog_color(typelog='debug', text='Exit module-{delete_config}', typemsg='Message', waydebug='%s' % (path_os(r'files/log/debug.log')), waygeneral='%s' % (path_os(r'files/log/general.log')), without_out_console=False)
        case False:
            for file in files : os.remove('%s' % (
                                                 path_os(r'files/config/%s' % (file))
                                                ))

def create_buffer():
    os.mkdir('%s' % (path_os(r'files/buffer')))
