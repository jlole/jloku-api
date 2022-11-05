import json
from sudoku import Board

class GoDoku:
  sudoku = Board()

  def generate_puzzle(self, difficulty):
    self.sudoku.generateQuestionBoardCode(difficulty)
    return json.dumps(self.sudoku.board)
