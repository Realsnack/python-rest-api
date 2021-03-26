import configparser
import json

def loadConfig(configName):
    config = configparser.ConfigParser()

    with open(configName, 'r') as f:
        config = json.load(f)

    return config


config = loadConfig('config.json')