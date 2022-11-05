from pymongo import MongoClient

class Database():
  client = MongoClient("mongodb+srv://jloku:l9RVIAS4hw0d6vnx@cluster0.dgbj2.mongodb.net/?retryWrites=true&w=majority")
  db = client['jloku']

  def get_daily(self):
    collection = self.db["daily_godokus"]
    item_details = collection.find()
    for item in item_details:
      return item['puzzle']
