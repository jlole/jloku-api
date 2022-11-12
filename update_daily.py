from jloku.sudoku import Board
from jloku.database import Database
from datetime import date
import json

the_date = date.today()
the_date = the_date.strftime("%d-%m-%Y")

daily_puzzle = json.loads(Board().generate_puzzle('2'))
daily_puzzle['date'] = the_date

Database().update_daily(daily_puzzle)
