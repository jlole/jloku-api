from flask import Flask
from flask import request
from godoku import GoDoku
from database import Database

app = Flask(__name__)

@app.route("/")
def api_home():
    return "Welcome to the jloku api!"

@app.route("/generate_board")
def generate_board():
    difficulty = request.args.get('difficulty')
    if difficulty == None or not difficulty.isnumeric() or int(difficulty) not in range(4):
        difficulty = 1
    print(difficulty)
    return GoDoku().generate_puzzle(int(difficulty))

@app.route("/get_daily_board")
def get_daily_board():
    return Database().get_daily()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
