import sys
import clingo

class SudokuApp(clingo.Application):

    def main(self, ctl, files):
        ctl.load("sudoku1.lp")

        for f in files:
            ctl.load(f)

        ctl.ground([("base", [])])
        ctl.solve()

    def print_model(self, model, printer):
        atoms = model.symbols(shown=True)
        atomsStr = [str(atom) for atom in atoms]
        atomsStr.sort()

        print(" ".join(atomsStr))

if __name__ == "__main__":
    app = SudokuApp()
    clingo.clingo_main(app, sys.argv[1:])