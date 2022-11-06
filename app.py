from flask import Flask
from flask import request
from sudoku import Board
from database import Database

app = Flask(__name__)


@app.route("/")
def api_home():
    return "Welcome to the jloku api!"


@app.route("/generate_board")
def generate_board():
    return Board().generate_puzzle(request.args.get('difficulty'))


@app.route("/get_daily_board")
def get_daily_board():
    return Database().get_daily()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
