import json

def loadConfig(path : str):
    jsondata = None
    with open(path, 'r') as f:
        jsondata = json.loads(f.read())
    return jsondata