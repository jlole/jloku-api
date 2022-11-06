import os
from pymongo import MongoClient
class Database():
  MONGO_USERNAME = os.getenv('MONGO_USERNAME')
  MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
  client = MongoClient("mongodb+srv://" + MONGO_USERNAME + ":" + MONGO_PASSWORD + "@cluster0.dgbj2.mongodb.net/?retryWrites=true&w=majority")
  db = client['jloku']

  def get_daily(self):
    collection = self.db["daily_godokus"]
    item_details = collection.find()
    for item in item_details:
      return {"puzzle":item['puzzle'],"solution":item['solution']}
