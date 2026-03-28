import sys
import clingo
from sudoku_board import Sudoku

class SudokuApp(clingo.Application):

    def main(self, ctl, files):
        ctl.load("sudoku1.lp")

        for f in files:
            ctl.load(f)

        ctl.ground([("base", [])])
        ctl.solve()

    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(str(sudoku))


if __name__ == "__main__":
    app = SudokuApp()
    clingo.clingo_main(app, sys.argv[1:])