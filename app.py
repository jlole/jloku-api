from flask import Flask
from godoku import GoDoku
from database import Database

app = Flask(__name__)

@app.route("/")
def api_home():
    return "Welcome to the jloku api!"

@app.route("/generate_board")
def generate_board():
    g = GoDoku()
    return g.generate_puzzle(1)

@app.route("/get_daily_board")
def get_daily_board():
    g = GoDoku()
    return Database().get_daily()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
