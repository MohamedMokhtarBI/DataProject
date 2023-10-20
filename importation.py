import pandas as pd 
import glob 
import json 
import configparser
from datetime import datetime as datetime

from dateutil.parser import parse
configpath="E:/DataProject/DataProject/configfile.ini"
config=configparser.ConfigParser()
config.read(configpath)
filepath=config['DATA']['SOURCE']


if __name__=="__main__":
    print(filepath)