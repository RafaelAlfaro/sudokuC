class Cvs_format:
    def __init__(self, cvs_string = ""):
        """
        constructor
        """
        self.cvs = cvs_string

    def get_sudoku_cvs(self):
        """
        Thie method gets the sudoku in cvs format
        """
        return self.cvs

    def put_sudoku_cvs(self, puzzle):
        self.cvs = puzzle

    def read_a_cvs_form_file(self, cvs_path):
        """
        This method read a sudoku in cvs format
        """
        try:
            cvs_file = open(cvs_path, "r")
            self.cvs = cvs_file.readline()
            cvs_file.close()
        except:
            return ("The file cannot be read")


    def write_to_cvs_file (self, file_path,puzzle):
        """
        This method write to file the cvs
        """
        try:
            cvs_file = open(file_path, "w")
            cvs_file.write(puzzle)
            cvs_file.close()
        except:
            return ("The file cannot be read")



    def verify_commas(self):
        """
        This method verify if the string has 8 commas in the position properly
        """
        size = len(self.cvs)
        for i in range(9, size,10):
            if (self.cvs[i]!= ','):
                print (self.cvs[i])
                return False
        return True


    def validate_sudoku_cvs(self, puzzle = ""):
        """
        This method accept a string with format cvs and remove the commas and
        return the sudoku in a line.
        """
        if puzzle == "": puzzle = self.cvs
        num_commas = self.cvs.count(',')
        size = len(self.cvs)
        if (size == 89)and(num_commas == 8):
            if (self.verify_commas()):
                return True
        return False

    def get_sudoku_cvs_to_str(self):
        """
        This method return in string format remove the commas
        """
        if(self.validate_sudoku_cvs()):
            puzzle = self.cvs.replace(',','')
            return puzzle
        return []

    def get_lines_cvs_file(self, cvs_path):
        """
        This method get all the cvs into the file
        """
        try:
            cvs_file = open(cvs_path, "r")
            lines = cvs_file.readlines()
            cvs_file.close()
            return lines
        except:
            return ("The file cannot be read")

    def change_to_cvs_format(self,puzzle, char_empty = '0'):
        """
        This method changes the string to csv format
        - The string should have 81 characters as minimum.

        """
        size = len (puzzle)
        if(size >= 81):
            puzzle = puzzle.replace('0',char_empty)
            puzzle = puzzle.replace('.',char_empty)
            puzzle = puzzle.replace('_',char_empty)

        return puzzle
