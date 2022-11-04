from flask import Flask
from godoku import GoDoku

app = Flask(__name__)

@app.route("/api")
def hello_world():
    return "jloku api!"

@app.route("/api/generate_board")
def generate_board():
    g = GoDoku()
    return g.generate_puzzle()

@app.route("/api/get_daily_board")
def get_daily_board():
    g = GoDoku()
    return g.get_daily_board()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
