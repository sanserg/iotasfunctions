import datetime as dt
import json
import pandas as pd
import numpy as np
import logging
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, func
from iotfunctions.db import Database
from iotfunctions.enginelog import EngineLogging

EngineLogging.configure_console_logging(logging.DEBUG)

'''
You can test functions locally before registering them on the server to
understand how they work.

Supply credentials by pasting them from the usage section into the UI.
Place your credentials in a separate file that you don't check into the repo. 

'''

with open('credentials.json', encoding='utf-8') as F:
    credentials = json.loads(F.read())
db_schema = None
db = Database(credentials=credentials)


db.unregister_functions(['NewFunction'])

