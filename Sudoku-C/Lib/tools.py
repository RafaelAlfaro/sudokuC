import string


class Tools:
    def __init__(self):
        pass

    def generate_matrix(self, rows, columns):
        """
        it generates a zero matrix
        row is the number of rows for the matrix
        col is the number of columns for the matrix
        """
        matrix =  []
        for row in range(rows):
            matrix.append([0] * columns)
        return matrix

    def convert_str_to_matrix(self, str_to_convert, row, col):
        """
        it receives an string and it returns a matrix
        str_to_convert is an string in order to convert a matrix
        row it is the max row for the matrix
        col it is the max column for the matrix
        """
        matrix =  self.generate_matrix(row, col)
        list_file =  []
        for element in str_to_convert:
            list_file.append(int(element))
        cont_col =  0
        cont_row =  0
        pos_list_file =  0
        for i in list_file:
            if cont_col ==  9:
                cont_row +=  1
                cont_col =  0
            matrix[cont_row][cont_col] =  list_file[pos_list_file]
            cont_col +=  1
            pos_list_file +=  1
        return matrix

    def convert_matrix_to_str(self, matrix_int):
        """
        This method converts a matrix to str
        """
        rows =  len(matrix_int)
        columns =  len(matrix_int[0])
        matrix_str =  []
        for row in range(rows):
            for col in range(columns):
                matrix_str.append(str(matrix_int[row][col]))
        str_tmp =  ''.join(matrix_str)
        return str_tmp

    def get_ABC(self, rows , columns):
        matrix_zero =  self.generate_matrix(rows, columns)
        var =  string.ascii_uppercase
        for f in range (rows):
            for col in range(columns):
                matrix_zero[f][col] =  var[col]
        return matrix_zero

    def display_board(self, board):
        rows =  len(board)
        columns =  len(board[0])
        ABC =  self.get_ABC(rows, columns)
        cont_ABC =  0
        for row in range(rows):
            if row ==  0:
                print "   ",
                for col2 in range(columns):
                    print "" + ABC[0][col2],
                    if col2 ==  2 or col2 ==  5: print " ",
                print ""
            if row ==  0 or row ==  3 or row ==  6 or row ==  rows:
                print "  - - - - - - - - - - - - -"
            for j in range(columns):
                if j ==  0:
                    print ABC[0][cont_ABC],
                    cont_ABC +=  1
                if j ==  0 or j ==  3 or j ==  6: print"|",

                if board[row][j] ==  0:
                    print ".",
                else:
                    print board[row][j],
                if j==  8: print "|"
            if row ==  8: print"  - - - - - - - - - - - - -"


    def count_zeros(self, matrix):
        rows =  len(matrix)
        columns =  len(matrix[0])
        cont_zeros =  0
        for row in range(rows):
            for col in range(columns):
                if matrix[row][col] ==  0:
                    cont_zeros +=  1
        return cont_zeros

    def verify_game_completed(self, game_matrix):
        if self.count_zeros(game_matrix) ==  0:
            return True
        else:
            return False

