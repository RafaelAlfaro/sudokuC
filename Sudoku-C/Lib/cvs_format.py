'''
Created on Jul 07, 2013
@author: Rafael Alfaro
'''
import time
class Cvs_format:
    def __init__(self, cvs_string=""):
        """
        This methos is the constructor of the object.
         Keyword arguments:
            cvs_string : the string to verify by default is empty
        """
        self.cvs = cvs_string

    def get_sudoku_cvs(self):
        """
        This method gets the value form object.
        return the value in self.cvs
        """
        return self.cvs

    def put_sudoku_cvs(self, puzzle):
        self.cvs = puzzle

    def read_a_cvs_form_file(self, cvs_path):
        """
        This method read a sudoku in cvs format
        Keyword arguments:
            cvs_path: The path of cvs
        """
        try:
            cvs_file = open(cvs_path, "r")
            self.cvs = cvs_file.readline()
            cvs_file.close()
        except:
            return ("The file cannot be read")

    def generate_name_cvs_file(self,file_name = ""):
        """ This function generate a name for the text file  using the date and time of the
            local computer.
        """
        get_time = time.strftime('%H%M%S%m%d%Y')
        if(file_name == ""):
            file_name = "sudoku_"+get_time+".cvs"
        else:
            file_name = name_of_file + "_"
            file_name += get_time+".cvs"
        return file_name

    def write_to_cvs_file (self, file_path,puzzle,result=""):
        """
        This method write to file the cvs
        Keyword arguments:
            file_path: path of out
            puzzle: the string to save in the file
        """
        try:
            file_path = file_path + "\\" +self.generate_name_cvs_file()
            cvs_file = open(file_path, "w")
            cvs_file.write(puzzle + "\n")
            if result !="":
               cvs_file.write(result + "\n")
            cvs_file.close()
        except:
            return ("The file cannot be read")


    def verify_commas(self):
        """
        This method verify if the string has 8 commas in the position properly
        Return: True if the format is correct
                False if the format is not correct
        """
        size = len(self.cvs)
        for i in range(9, size,10):
            if (self.cvs[i]!= ','):
                return False
        return True


    def validate_sudoku_cvs(self, puzzle=""):
        """
        This method accept a string with format cvs and remove the commas and
        return the sudoku in a line.
         Keyword arguments:
            puzzle : the sudoku to validate
         Return:
            True : if the string is correct
            False : if the string is not correct

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


    def remove_eol(self, puzzle):
        """
        This method remove the end of fole
        """
        size = len(puzzle)-1
        if puzzle[size]=='\n':
            puzzle =  puzzle [:-1]
        self.cvs = puzzle
        return puzzle

    def change_to_cvs_format(self,puzzle, char_empty = '0'):
        """
        This method changes the string to csv format
        - The string should have 81 characters as minimum.
        return a string with sudoku in cvs format

        """
        size = len(puzzle)
        if(size >= 81):
            self.remove_eol(puzzle)
            puzzle = puzzle.replace('0',char_empty)
            puzzle = puzzle.replace('.',char_empty)
            puzzle = puzzle.replace('_',char_empty)
            self.cvs = ""
            for i in range(size):
                if i in [9,18,27,36,45,54,63,72]:
                   self.cvs += ','
                self.cvs += puzzle[i]
        return self.cvs
