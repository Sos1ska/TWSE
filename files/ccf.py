import io, zipfile
from json import dump, dumps, load, loads
from important_func import load_pyc_files

def CreateSYSConfig():
    ram=io.BytesIO()
    structure = load_pyc_files(r'structure_configs.pyc')
    with zipfile.ZipFile(ram, 'w') as fileinram:
        with io.BytesIO() as json_ram:
            data=dumps(structure.systemC())
            json_ram.write(data.encode())
            json_ram.seek(0)
            
            fileinram.writestr('system.json', json_ram.read())
    with open(r'files\buffer\system.zip', 'wb') as file:
        ram.seek(0)
        file.write(ram.read())
