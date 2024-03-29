import os
from pymongo import MongoClient
import pymongo

class Database():
  MONGO_USERNAME = os.getenv('MONGO_USERNAME')
  MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')

  if MONGO_USERNAME and MONGO_PASSWORD:
    client = MongoClient("mongodb+srv://" + MONGO_USERNAME + ":" + MONGO_PASSWORD + "@cluster0.dgbj2.mongodb.net/?retryWrites=true&w=majority")
  else:
    client = MongoClient("mongodb://root:rootpassword@jloku-mongo:27017")
    
  db = client['jloku']

  def get_daily(self):
    collection = self.db["daily_godokus"]
    item_details = collection.find().sort('_id', pymongo.DESCENDING)
    daily = item_details.next()
    return {'date': daily['date'], 'puzzle': daily['puzzle'], 'solution': daily['solution']}

  def update_daily(self, daily_puzzle):
    collection = self.db["daily_godokus"]
    collection.insert_one(daily_puzzle)
