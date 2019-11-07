import datetime as dt
import json
import pandas as pd
import numpy as np
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, func
from iotfunctions.base import BaseTransformer
from iotfunctions.metadata import EntityType
from iotfunctions.db import Database
from iotfunctions import ui

with open('credentials.json', encoding='utf-8') as F:
  credentials = json.loads(F.read())
db_schema = None
db = Database(credentials=credentials)


from custom.functions import MultiplyByFator
db.register_functions([MultiplyByFator])


from custom.functions import MyCustomFunction
db.register_functions([MyCustomFunction])