import os
import integrator
from menus import Menus
import time
from tools import Tools

class SudokuPlay():
    def __init__(self):
        self.new_tool = Tools()
        self.matrix_play = []
        self.row = 0
        self.column = 0
        self.value = 0
        self.new_menu = Menus()
        self.return_game = ""
        self.boards = integrator.integrator()

    def print_sub_menu_play(self):
        self.new_menu.print_sub_menu_play()

    def start_end_menus(self, matrix_play, menu):
        os.system('cls')
        self.new_tool.display_board(matrix_play)
        if menu == "play":
            self.print_sub_menu_play()
            return raw_input("Make your play:")
        elif menu == "read":
            self.new_menu.print_sub_menu_read()
            return raw_input("Choose your option:")
        elif menu == "save":
            self.new_menu.print_sub_menu_save()
            return raw_input("Choose your option:")

    def verify_read_key_str(self, read_key, pos):
        ABC = self.new_tool.get_ABC(9, 9)
        list_tmp = list(read_key)
        try:
            if ABC[0].index(list_tmp[pos]) >= 0:
                return True
            else:
                return False
        except:
            return False

    def get_parse_str(self, read_key, pos):
        list_tmp = list(read_key)
        return list_tmp[pos]


    def verify_read_key_int(self, read_key, pos):
        list_tmp = list(read_key)

        try:
            if len(list_tmp) >= 4:
                return False
            else:
                if int(list_tmp[2]) in range(0, 10):
                    self.value = int(list_tmp[2])
                    return True
                else:
                    return False
        except: return False

    def set_possiton(self, read_key):
        list_tmp = list(read_key)
        self.row = ord(list_tmp[0]) - 65
        self.column = ord(list_tmp[1]) - 65

    def verify_busy(self, matrix, rows, columns):

        if matrix[rows][columns] == 0:
            return False
        else: return True

    def change_value_in_matrix(self, matrix, row, column, value):
        matrix[row][column] = str(value)
        return matrix


    def play_the_game(self, puzzle):
        self.boards.load_sudoku()
        puzzle = self.boards.get_original_sudoku()
        self.matrix_play = self.new_tool.convert_str_to_matrix(puzzle, 9, 9)
        read_key = self.start_end_menus(self.matrix_play,"play")
        while read_key != "Q":
            parse_row = self.verify_read_key_str(read_key, 0)
            parse_column = self.verify_read_key_str(read_key, 1)
            parse_value = self.verify_read_key_int(read_key, 2)

            if parse_row and parse_column and parse_value:
                self.set_possiton(read_key)

                if not self.verify_busy(self.matrix_play, self.row, self.column):
                    self.matrix_play = self.change_value_in_matrix(self.matrix_play, self.row, self.column, self.value)
                    self.return_game = self.new_tool.convert_matrix_to_str(self.matrix_play)
                else:
                    raw_input("That point is busy, make another play")
            elif read_key == "g":
                self.boards.load_sudoku()
                puzzle = self.boards.get_original_sudoku()
                self.matrix_play = self.new_tool.convert_str_to_matrix(puzzle, 9, 9)
            elif read_key == "r":
                self.print_sub_menu_read()
            elif read_key == "h":
                currently_game = self.new_tool.convert_matrix_to_str(self.matrix_play)
                currently_game = self.boards.get_hint(currently_game)
                self.matrix_play = self.new_tool.convert_str_to_matrix(currently_game, 9, 9)
            elif read_key == "v":
                puzzle = self.boards.get_solved_puzzle()
                print puzzle
                self.matrix_play = self.new_tool.convert_str_to_matrix(puzzle, 9, 9)
            elif read_key == "t":
                puzzle = self.boards.get_original_sudoku()
                self.matrix_play = self.new_tool.convert_str_to_matrix(puzzle, 9, 9)
            elif read_key == "s":
                self.print_sub_menu_save()
            elif read_key == "q":
                if raw_input("do you really want to quit(y/n)? ") == "y":
                    break
            else:
                raw_input("Make another play. Review the upper case and value")


            read_key = self.start_end_menus(self.matrix_play,"play")

    def print_sub_menu_read(self):
        read_key = self.start_end_menus(self.matrix_play,"read")

        while read_key != "B":
            if read_key == "t":
               path_file = self.get_path_from_console("txt")
               puzzle = self.boards.read_txt_file(path_file)
               self.matrix_play = self.new_tool.convert_str_to_matrix(puzzle, 9, 9)
            elif read_key == "v":
               path_file = self.get_path_from_console("cvs")
               puzzle = self.boards.read_cvs_file(path_file)
               self.matrix_play = self.new_tool.convert_str_to_matrix(puzzle, 9, 9)
            elif read_key == "c":
                #print "you press key %s" %(read_key)
                self.load_from_console()
            elif read_key == "b":
                break
            else:
                read_key = raw_input("choose another option.")

            read_key = self.start_end_menus(self.matrix_play,"read")

    def print_sub_menu_save(self):
        read_key = self.start_end_menus(self.matrix_play,"save")
        currently_game = self.boards.get_original_sudoku()
        while read_key != "B":
            if read_key == "t":
                self.boards.save_txt(currently_game)

            elif read_key == "c":
                self.boards.save_cvs(currently_game)
            elif read_key == "h":
                 self.boards.save_html(currently_game)
            elif read_key == "d":
                 self.boards.save_default()
            elif read_key == "b":
                break
            else:
                read_key = raw_input("choose another option.")

            read_key = self.start_end_menus(self.matrix_play,"save")

    def verify_numbers(self, numbers_string):
        pass

    def load_from_console(self):
        puzzle = raw_input("Introduce the game in a single string:")
        if len(puzzle) == 81:
            self.matrix_play = self.new_tool.convert_str_to_matrix(puzzle, 9, 9)
        else:
            raw_input("wrong input, try it again")


    def get_path_from_console(self,type_input):
        path_file = raw_input("Introduce the path of the game("+type_input+"):")
        return path_file


