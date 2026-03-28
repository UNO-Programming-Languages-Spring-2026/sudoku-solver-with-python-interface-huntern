import sys
import clingo
from sudoku_board import Sudoku

class Context:
    def __init__(self, board: Sudoku):
        self.board = board
    def initial(self) -> list[clingo.symbol.Symbol]:
        symbolList = []
        for (row, col), val in self.board.sudoku.items():
            symbolList.append(
                clingo.Function(
                    "",
                    [
                        clingo.Number(row),
                        clingo.Number(col),
                        clingo.Number(val)
                    ]
                )
            )
        return symbolList

class SudokuApp(clingo.Application):

    def main(self, ctl, files):
        with open(files[0]) as f:
            content = f.read()
        sudoku = Sudoku.from_str(content)
        context = Context(sudoku)
        ctl.load("sudoku1.lp")
        ctl.load("sudoku_py.lp")

        ctl.ground([("base", [])], context = context)
        ctl.solve()


    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(str(sudoku))


if __name__ == "__main__":
    app = SudokuApp()
    clingo.clingo_main(app, sys.argv[1:]) 