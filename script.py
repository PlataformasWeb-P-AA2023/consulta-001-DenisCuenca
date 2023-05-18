import pandas as pd
import pymongo as pm
from pprint import pprint

# read data: 
tennis_tournaments_data = pd.read_csv("./atp_tennis.csv")

# transforma CSV data into BSON
tennis_tournaments_data = tennis_tournaments_data.to_dict("records")

# create mongodb conection
MongoClient = pm.MongoClient("mongodb://localhost:27017/")
tennis_tournaments_collection = MongoClient["tennis_tournaments"]["tournaments"]

# insert data:
tennis_tournaments_collection.insert_many(tennis_tournaments_data)

# list data:
for x in tennis_tournaments_collection.find({}):
	pprint(x)