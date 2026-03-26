from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        for row in range(1, 10):
            for col in range(1, 10):
                val = self.sudoku[(row, col)]
                s += str(val)
                if col < 9:
                    if col % 3 == 0:
                        s += "  "
                    else:
                        s += " "
            s += "\n"
            if row % 3 == 0 and row < 9:
                s += "\n"
        #print(s)
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        for atom in model.symbols(shown = True):
            if atom.name == "sudoku" and len(atom.arguments) == 3:
                row = atom.arguments[0].number
                col = atom.arguments[1].number
                val = atom.arguments[2].number
                sudoku[(row, col)] = val
        return cls(sudoku)
