from menus import Menus
import os
import xml.etree.ElementTree as xmltree
from tools import Tools
from sudoku_play import SudokuPlay
from configuration import Configuration

class ConsolePresentation:
    def __init__(self, puzzle):
        self.sudoku_game = puzzle
        self.new_tool = Tools()
        self.matrix = self.new_tool.convert_str_to_matrix(self.sudoku_game, 9, 9)
        self.new_menus = Menus()
        self.new_configuration = Configuration()
        self.new_sudoku_play = SudokuPlay()
        self.path_of_file = os.getcwd() + "\\configurations\\"
        self.matrix_play = self.matrix
        self.row = 0
        self.column = 0
        self.value = 0
        self.algorithm = ""
        self.difficulty = ""
        self.solved_out_put = ""
        

    def read_xml(self, file_name):
        """
        It receives an xml file and return root, it has the xml file data
        """
        try:
            self.tree = xmltree.parse(self.path_of_file + file_name)
        except:
            self.tree = xmltree.parse(self.path_of_file+self.name_of_file)

        self.root = self.tree.getroot()

        return self.root

    def get_difficulty_levels(self, root):
        """
        This method we did because we start writing code instead write a unit TC before; so this is an example of what we should not do it.
        """
        list_tmp = ""
        matrix = []
        for levels in root.iter('level'):
            xml_read = levels.attrib
            id_xml = xml_read['id']
            name_xml = xml_read['name']
            min_xml = xml_read['min']
            max_xml = xml_read['max']
            list_tmp = id_xml, name_xml, min_xml, max_xml
            matrix.append(list_tmp)
        return matrix

    def start_end_menus(self, menu):
        os.system('cls')
        self.new_tool.display_board(self.matrix)

        if menu == "main":
            self.new_menus.print_main_menu()
        elif menu == "game":
            self.new_menus.print_sub_menu_game()
        elif menu == "play":
            self.new_menus.print_sub_menu_play()
        elif menu == "read":
            self.new_menus.print_sub_menu_read()
        elif menu == "save":
            self.new_menus.print_sub_menu_save()
        elif menu == "options":
            self.new_menus.print_sub_menu_options()
        elif menu == "algorithm":
            self.new_menus.print_sub_menu_algorithm()
        elif menu == "difficulty":
            self.new_menus.print_list_difficulty()
            self.new_menus.print_sub_menu_difficulty()
        elif menu == "solved_out_put":
            self.new_menus.print_sub_menu_solved_out_put()
        elif menu == "edit":
            self.new_menus.print_sub_menu_edit()

        if menu == 'play':
            return raw_input("make your play: ")
        else:
            return raw_input("choose: ")

    def count_zeros(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        cont_zeros = 0
        for row in range(rows):
            for col in range(columns):
                if matrix[row][col] == 0:
                    cont_zeros += 1
        return cont_zeros

    def verify_game_completed(self, game_matrix):
        if self.count_zeros(game_matrix) == 0:
            return True
        else:
            return False


    def print_main_menu(self, puzzle):
        read_key = self.start_end_menus("main")

        while read_key != "X":
            if read_key == "p":
                self.new_sudoku_play.play_the_game(puzzle)
            elif read_key == "o":
                self.print_sub_menu_options()
            elif read_key == "x":
                print ""
                print "!!! Game Over !!!, ",
                print "you press key %s..." %(read_key)
                break
            else:
                read_key = raw_input("choose another option.")

            read_key = self.start_end_menus("main")

    def print_sub_menu_game(self):
        read_key = self.start_end_menus("game")

        while read_key != "B":
            if read_key == "p":
                self.play_the_game()
            elif read_key == "g":
                print "you press key %s" %(read_key)
            elif read_key == "l":
                print "You press key %s" % read_key
            elif read_key == "r":
                self.print_sub_menu_read()
            elif read_key == "s":
                self.print_sub_menu_save()
            elif read_key == "t":
                print "you press key %s" %(read_key)
            elif read_key == "b":
                break
            else:
                read_key = raw_input("choose another option.")

            read_key = self.start_end_menus("game")

    def print_sub_menu_read(self):
        read_key = self.start_end_menus("read")

        while read_key != "B":
            if read_key == "t":
                print "you press key %s" %(read_key)
            elif read_key == "v":
                print "you press key %s" %(read_key)
            elif read_key == "c":
                print "you press key %s" %(read_key)
            elif read_key == "b":
                break
            else:
                read_key = raw_input("choose another option.")

            read_key = self.start_end_menus("read")

    def print_sub_menu_save(self):
        read_key = self.start_end_menus("save")

        while read_key != "B":
            if read_key == "t":
                print "You press key %s" % read_key
            elif read_key == "c":
                print "you press key %s" %(read_key)
            elif read_key == "h":
                print "You press key %s" % read_key
            elif read_key == "b":
                break
            else:
                read_key = raw_input("choose another option.")

            read_key = self.start_end_menus("save")

    def print_sub_menu_options(self):
        read_key = self.start_end_menus("options")

        while read_key != "B":
            if read_key == "a":
                self.print_sub_menu_algorithm()
            elif read_key == "d":
                self.print_sub_menu_difficulty()
            elif read_key == "v":
                self.print_sub_menu_solved_out_put()
            elif read_key == "b":
                break
            else:
                read_key = raw_input("choose another option.")

            read_key = self.start_end_menus("options")

    def print_sub_menu_algorithm(self):
        read_key = self.start_end_menus("algorithm")

        while read_key != "B":
            if read_key == "k":
                self.algorithm = "backtracking"
                self.new_configuration.modify_value_in_xml(self.algorithm,"algorithm")
                raw_input ("you chose " +self.algorithm + " Algorithm")
                break
            elif read_key == "n":
                self.algorithm = "peternorvig"
                self.new_configuration.modify_value_in_xml(self.algorithm,"algorithm")
                raw_input ("you chose " + "Peter Norvig" + " Algorithm")
                break
            elif read_key == "i":
                self.algorithm = "recursive"
                self.new_configuration.modify_value_in_xml(self.algorithm,"algorithm")
                raw_input ("you chose " +self.algorithm + " Algorithm")
                break
            elif read_key == "b":
                break
            else:
                read_key = raw_input("choose another option.")

            read_key = self.start_end_menus("algorithm")

    def print_sub_menu_difficulty(self):
        read_key = self.start_end_menus("difficulty")
        difficulty_matrix = self.new_menus.get_difficulty_matrix()

        while read_key != "B":
            if read_key == "e":
                self.print_sub_menu_edit()
            try:
                if read_key == "e":
                    self.print_sub_menu_edit()
                elif read_key == "0":
                    self.difficulty = difficulty_matrix[0][1]
                    self.new_configuration.modify_value_in_xml(self.difficulty,"difficulty")
                    raw_input ("You chose " + self.difficulty + " as difficulty level") 
                    break
                elif read_key == "1":
                    self.difficulty = difficulty_matrix[1][1]
                    self.new_configuration.modify_value_in_xml(self.difficulty,"difficulty")
                    raw_input ("You chose "+ self.difficulty + " as difficulty level") 
                    break
                elif read_key == "2":
                    self.difficulty = difficulty_matrix[2][1]
                    self.new_configuration.modify_value_in_xml(self.difficulty,"difficulty")
                    raw_input ("You chose "+ self.difficulty + " as difficulty level") 
                    break
                elif read_key == "3":
                    self.difficulty = difficulty_matrix[3][1]
                    self.new_configuration.modify_value_in_xml(self.difficulty,"difficulty")
                    raw_input ("You chose "+ self.difficulty + " as difficulty level") 
                    break
                elif read_key == "4":
                    self.difficulty = difficulty_matrix[4][1]
                    self.new_configuration.modify_value_in_xml(self.difficulty,"difficulty")
                    raw_input ("You chose "+ self.difficulty + " as difficulty level") 
                    break
                elif read_key == "5":
                    self.difficulty = difficulty_matrix[5][1]
                    self.new_configuration.modify_value_in_xml(self.difficulty,"difficulty")
                    raw_input ("You chose "+ self.difficulty + " as difficulty level") 
                    break
                elif read_key == "b":
                    break
                else:
                    read_key = raw_input("choose another option.")
            except:
                raw_input("Choose another option")

            read_key = self.start_end_menus("difficulty")
            
    def print_sub_menu_solved_out_put(self):
        read_key = self.start_end_menus("solved_out_put")
        difficulty_matrix = self.new_menus.get_difficulty_matrix()

        while read_key != "B":
            if read_key == "e":
                self.print_sub_menu_edit()
            try:
                if read_key == "t":
                    self.solved_out_put = "txt"
                    self.new_configuration.modify_value_in_xml(self.solved_out_put,"solver_output_type")
                    raw_input ("You chose " + self.solved_out_put + " as solver output type") 
                    break
                elif read_key == "c":
                    self.solved_out_put = "csv"
                    self.new_configuration.modify_value_in_xml(self.solved_out_put,"solver_output_type")
                    raw_input ("You chose "+ self.solved_out_put + " as solver output type") 
                    break
                elif read_key == "h":
                    self.solved_out_put = "html"
                    self.new_configuration.modify_value_in_xml(self.solved_out_put,"solver_output_type")
                    raw_input ("You chose "+ self.solved_out_put + " as solver output type ") 
                    break
                elif read_key == "b":
                    break
                else:
                    read_key = raw_input("choose another option.")
            except:
                raw_input("Choose another option")

            read_key = self.start_end_menus("difficulty")

    def print_sub_menu_edit(self):
        read_key = self.start_end_menus("edit")

        while read_key != "B":
            if read_key == "n":
                print "You press key %s" % read_key
            elif read_key == "c":
                print "you press key %s" %(read_key)
            elif read_key == "b":
                break
            else:
                read_key = raw_input("choose another option.")

            read_key = self.start_end_menus("edit")

    def run_app(self, puzzle):
        self.print_main_menu(puzzle)

