class TestSudoku:
    def __init__(self):
        pass

    def try_sudoku(self, sudoku, assigned, row, col):
        """
        it test the sudoku matrix trying the possible
        sudoku it is a sudoku matrix that it is going to be resolved
        assigned it is a variable that contain the possible numbers in order to resolve the sudoku
        row is a position row for the matrix
        col is a position column for the matrix
        """
        rows = len(sudoku)
        cols = rows
        if sudoku[row][col] != 0:
            return([])
        else:
            result = []
            for n in range(1, rows+1):
                existe = False
                for l in range(0, rows):
                    if sudoku[l][col] == n:
                        existe = True
                        break
                for c in range(0, cols):
                    if sudoku[row][c] == n:
                        existe = True
                        break
                aux_row = (row/3)*3
                aux_column = (col/3)*3
                for r in range(3):
                   for c in range(3):
                        if assigned != [] :
                            for asig in assigned:
                                if sudoku[aux_row + r][aux_column + c]==n:
                                    existe = True
                                if asig[0] == aux_row + r and asig[1] == aux_column +c and asig[2] == n:
                                    existe = True
                for asig in assigned:
                    if asig[0] == row and asig[2] == n:
                        existe = True
                        break
                    if asig[1] == col and asig[2] == n:
                        existe = True
                        break
                if not existe:
                    result.append(n)
            if result == []:
                result = [-1]
            return result
