import os, sys, zipfile

def load_pyc_files(filepath):
    path, fname = os.path.split(filepath)
    module, _ = os.path.splitext(fname)
        
    if path not in sys.path:            
        sys.path.insert(0, path)
        
    return __import__(module)

def unzip_config():
    with zipfile.ZipFile(r'files\buffer\color.zip') as archive1:
        archive1.extractall(r'files\config')
    with zipfile.ZipFile(r'files\buffer\system.zip') as archive2:
        archive2.extractall(r'files\config')
        
def delete_config():
    files = ['system.json', 'color.json']
    for file in files:
        os.remove(r'files\config\%s' % (file))
