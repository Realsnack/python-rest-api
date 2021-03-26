import uvicorn
import configparser
import json


def loadConfig(configName):
    config = configparser.ConfigParser()

    with open(configName, 'r') as f:
        config = json.load(f)

    return config


if (__name__ == '__main__'):
    config = loadConfig('start.json')
    uvicorn.run("main:app", host=config["Host"], port=int(config["Port"]),
                log_level=config["Log_level"], reload=config["Reload"])
