import configparser
import os

ROOT_DIR=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

CONFIG_PATH=os.path.join(ROOT_DIR, 'Configurations', 'config.ini')

config=configparser.RawConfigParser()
config.read(CONFIG_PATH)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info', 'BaseUrl')
        return url
