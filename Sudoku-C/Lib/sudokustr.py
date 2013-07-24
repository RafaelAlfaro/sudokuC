'''
Created on Jul 07, 2013
@author: Rafael Alfaro
'''
class SudokuStr:
    def __init__(self,sudoku_str = "" , char_empty = '0'):
        self.sudoku_str = sudoku_str
        self.long = len (self.sudoku_str)
        self.char_empty = char_empty

    def get_length(self):
        return(self.long)

    def verify_only_num(self):
        aux = self.sudoku_str.isdigit()
        return(aux)

    def get_81_characters(self,size = 81):
        """
        This method gets the 81 first characters and remove the character "\n"
        """
        self.sudoku_str = self.sudoku_str[0:size]
        self.long = len (self.sudoku_str)
        return(self.sudoku_str)

    def print_values(self):
        """
        This merthod print the values in the object
        """
        print("String :" + self.sudoku_str)
        print("Length :" + str(self.long))
        print("Holes :" + self.char_empty)


    def get_zero_number(self,char):
        """
            This method get number of holes in the puzzle
        """
        return(self.sudoku_str.count(char))

    def verify_string_to_sudoku(self):
        """
            This method verify if the string has 81 characters and
        """
        length = self.get_length()
        if (length >= 80):
            self.sudoku_str = self.get_81_characters()
            if (not(self.verify_only_num())):
                self.sudoku_str = self.sudoku_str.replace('0',self.char_empty)
                self.sudoku_str = self.sudoku_str.replace('.',self.char_empty)
                self.sudoku_str = self.sudoku_str.replace('_',self.char_empty)
                return(True)
            else:
                return(False)

    def put_a_sring(self, sudoku_str,char_empty = '0'):
        """
        This method put a new puzle to verify
        """
        self.sudoku_str = sudoku_str
        self.long = len (self.sudoku_str)
        self.char_empty = char_empty

    def get_str(self):
        """
        This method get the sring of the object
        """
        return(self.sudoku_str)

