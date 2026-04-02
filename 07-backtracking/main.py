import os
import sys
import numpy as np


class SudokuSolver:
    def __init__(self):
        self.field = np.zeros([9, 9], dtype=int)

    def load(self, file_path: str) -> None:

        # list of lists (rows)
        loaded_rows: list[list[int]] = []
        # TODO implement loading of the file
        with(open(file_path, "r", encoding="utf8") as file):
            for line in file:
                temp_line = line.strip().split(";")
                ret = []
                for num in temp_line:
                    ret.append(int(num))
                loaded_rows.append(ret)
        # convert nested list to numpy array
        self.field = np.array(loaded_rows)
        print(self.field)

    def check_sequence(self, sequence: np.ndarray) -> bool:
        sequence_zero = sequence[sequence != 0]
        return(len(set(sequence_zero)) == len(sequence_zero))

    def check_row(self, row_index: int) -> bool:
        row = self.field[row_index,:]
        return(self.check_sequence(row))

    def check_column(self, column_index: int) -> bool:
        col = self.field[:, column_index]
        return(self.check_sequence(col))


    def check_block(self, row_index: int, column_index: int) -> bool:
        row_start = (row_index//3)*3
        col_start = (column_index//3)*3
        sequence = self.field[row_start:row_start+3,col_start:col_start+3].reshape(-1)
        return(self.check_sequence(sequence))


    def check_one_cell(self, row_index: int , column_index: int) -> bool:
        return self.check_row(row_index) and self.check_column(column_index) and self.check_block(row_index, column_index)

    def get_empty_cell(self) -> tuple[int, int] | None:
        """ Gets the coordinates of the next empty field. """
        for col in range(self.field.shape[0]):
            for row in range(self.field.shape[1]):
                if(self.field[col, row] == 0):
                    return(col,row)
        return None

    def solve(self) -> bool:
        """ Recursively solves the sudoku. """
        index = self.get_empty_cell()
        if(index == None):
            return(True)

        row, col = index

        for i in range(1, 10):
            self.field[row, col] = i
            if(self.check_one_cell(row, col) and self.solve()):
                return(True)
            print("-------")
            print(self.field)

        self.field[row, col] = 0
        return False


def main() -> None:
    sudoku_solver = SudokuSolver()
    sudoku_solver.load("07-backtracking\\sudoku.csv")

    sudoku_solver.field = sudoku_solver.field[0:3, 3:6]

    sudoku_solver.solve()
    print("----------FINISHED----------")
    print(sudoku_solver.field)
    """
    sudoku_solver.field[2,2] = 6
    print(sudoku_solver.field)
    for col in range(9):
        for row in range(9):
            print(f"{col}:{row}, {sudoku_solver.check_one_cell(col, row)}")

    print(sudoku_solver.get_empty_cell())
    """

if __name__ == "__main__":
    main()
