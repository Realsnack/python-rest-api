import uvicorn
import configparser
import json


def load_config(configName):
    config = configparser.ConfigParser()

    with open(configName, 'r') as f:
        config = json.load(f)

    return config


if (__name__ == '__main__'):
    config = load_config('start.json')
    uvicorn.run("main:app", host=config["Host"], port=int(config["Port"]),
                log_level=config["Log_level"], reload=config["Reload"])
