import json
from sudoku import Board

class GoDoku:
  board_structure = [[1,1,1,2,2],[1,1,3,2,2],[4,3,3,3,2],[4,4,3,5,5],[4,4,5,5,5]]
  daily = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [5, 0, 3, 4, 1], [2, 0, 5, 0, 0], [1, 3, 4, 0, 2]]
  sudoku = Board()

  def get_daily_board(self):
    v = self.daily
    return json.dumps(v)

  def generate_puzzle(self, difficulty):
    self.sudoku.generateQuestionBoardCode(difficulty)
    return json.dumps(self.sudoku.board)
