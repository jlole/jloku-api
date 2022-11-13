from jloku.sudoku import Board
from jloku.database import Database
import datetime
import json
import pytz

timezone = pytz.timezone("Europe/Amsterdam")
the_date = datetime.datetime.now()
the_date = timezone.localize(the_date)
the_date = the_date.strftime("%d-%m-%Y")

daily_puzzle = json.loads(Board().generate_puzzle('2'))
daily_puzzle['date'] = the_date

Database().update_daily(daily_puzzle)
