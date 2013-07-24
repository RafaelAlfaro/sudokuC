import time
class FileTxt:
    def __init__(self):
        self.file_path = ""
        self.file_name = ""
        self.file_content = ""

    def define_path(self, file_path):
        """ Function that receives the path where there is the text file.
            Keyword arguments:
                file_path -- path where there is the text file.
        """
        self.file_path = file_path
        return self.file_path

    def read_txt_file(self):
        """ Open  a file that contains the game in the form of nine characters and a \n.
        """
        try:
            f = open(self.file_path, "r")
            self.file_content = f.read()
            f.close()
            return self.file_content
        except:
            return []

    def parse_txt_file_on_a_single_line(self):
        """ Function that converts the contents of the text file in a single line without \n.
            and  saves it to a new text file.
        """
        final_string = ""
        if not(self.file_content == ""):
            final_string = self.file_content.replace("\n", "")
            if self.get_number_of_characters(final_string) :
                if self.get_if_is_digit(final_string):
                    return final_string

    def generate_name_txt_file(self,name_of_file = ""):
        """ This function generate a name for the text file  using the date and time of the
            local computer.
        """
        get_time = time.strftime('%H%M%S%m%d%Y')
        if(self.file_name == ""):
            self.file_name = "sudoku_" + get_time + ".txt"
        else:
            self.file_name = name_of_file + "_"
            self.file_name += get_time +".txt"
        return self.file_name

    def create_txt_file(self, puzzle, result="", name_of_file=""):
        """ Create a new text file to save the game in the new format.
            Keyword arguments:
                content -- Is the game on a string unresolved without \n
        """
        self.file_name = name_of_file
        self.generate_name_txt_file(name_of_file)
        path_txt = self.file_path+self.file_name
        try:
            print (path_txt)
            f = open(path_txt, "w")
            f.write(puzzle + "\n")
            if result !="":
               f.write(result + "\n")
            f.close()
            return True
        except:
            return False


    def get_quantity_of_zeros(self, content):
        """ Function that counts the number of zeros which has a game and accordingly
            determine the difficulties.
        """
        quantity_of_zeros = content.count("0")
        return quantity_of_zeros

    def get_number_of_characters(self, content):
        """ Function that valid if the game with new formatted contains 81 characters.

            Keyword arguments:
                content -- Is the game on a string unresolved without \n
        """
        if len(content) == 81: return True
        else: return False

    def get_if_is_digit(self, content):
        """ Function that valid if the game with new formatted contains only digits.

            Keyword arguments:
                content -- Is the game on a string unresolved without \n
        """
        if content.isdigit():
             return True
        else:
             return False




