from flask import Flask
from flask import request
from jloku.sudoku import Board
from jloku.database import Database

app = Flask(__name__)


@app.route("/")
def api_home():
    return "Welcome to the jloku api!"


@app.route("/get-new-puzzle")
def generate_board():
    return Board().generate_puzzle(request.args.get('difficulty'))


@app.route("/get-daily-puzzle")
def get_daily_board():
    return Database().get_daily()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
