import configparser
import json

def load_config(configName):
    config = configparser.ConfigParser()

    with open(configName, 'r') as f:
        config = json.load(f)

    return config


config = load_config('config.json')