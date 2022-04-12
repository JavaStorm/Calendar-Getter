import json

def loadConfig(path : str):
    rawdata = ""
    jsondata = None
    with open(path, 'r') as f:
        rawdata = f.read()
    jsondata = json.load(rawdata)
    return jsondata