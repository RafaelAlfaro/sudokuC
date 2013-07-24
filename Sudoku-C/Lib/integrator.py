'''
Created on Jul 23, 2013
@author: Rafael Alfaro
'''
import random
import configuration
import cvs_format
import file_txt
import htmlsudoku
import peter_algorithm
import recursive
import resolve
import sudoku

class integrator:
    def __init__(self):
        """
           This method initialize the xml and values
        """
        self.puzzle_original = ""
        self.puzzle_solved = ""
        self.puzzle_playing = ""
        self.xml_config = configuration.Configuration()
        self.xml_config.load_xml_data()
        self.min_zeros,self.max_zeros = self.xml_config.get_max_and_min_difficulty()

    def get_original_sudoku(self):
        """
           Return the original puzzle generated
        """
        return self.puzzle_original

    def get_solved_puzzle(self):
        """
           Return the solved puzzle
        """
        return self.puzzle_solved

    def get_playing_puzzle(self):
        """
           Return the currently puzzle
        """
        return self.puzzle_playing

    def load_sudoku(self):
        """
           This method get a new game
        """
        game = sudoku.Sudoku()
        validator = True
        while validator:
          game.get_sudoku(int(self.min_zeros),int(self.max_zeros))
          self.puzzle_original = game.get_puzzle_srt()
          if self.puzzle_original.find("None") == -1:
              validator = False
        self.puzzle_solved = game.get_solution_str()
        self.puzzle_playing = ""


    def convert_content_in_list(self, content):
        """
           Return a list
           Keyword arguments:
               content - this have the puzzle in a string and return a list
        """
        return list(content)

    def parsed_list_in_string(self, content_list):
        """
           Function that converts the list that contains the game with hint on a string.
           Keyword arguments:
           content_list -- List that contains the hint.
        """
        puzzle = ''.join(content_list)
        return puzzle

    def get_hint(self, unresolved_game):
        """ Function that interacts random into the list that contains the game is not resolved
            with the list containing the game resolved.
            If the value is zero, look at the game list solved the same position and modifies the
            unresolved list with the new hint.

            Keyword arguments:
                unresolved_content -- string of numbers that can contain the game unresolved.
                solved_content -- string of numbers that can contain the game resolved.
        """
        puzzle_playing = unresolved_game
        solved_content = self.puzzle_solved
        size = len (unresolved_game)
        list_with_zeros = self.convert_content_in_list(unresolved_game)
        list_without_zeros = self.convert_content_in_list(self.puzzle_solved)
        verification = True
        while(list_with_zeros.count("0") and verification):
            random_position = random.randint(0, size - 1)
            value_to_search = list_with_zeros[random_position]
            if value_to_search == "0":
                list_with_zeros[random_position] = list_without_zeros[random_position]
                self.puzzle_playing = self.parsed_list_in_string(list_with_zeros)
                verification = False
        return self.puzzle_playing

    def save_txt(self, puzzle):
        """
           This method creates a puzzle in txt format
           Keyword arguments:
                   puzzle : This variable has a sudoku game and save a txt format
        """
        txt_format = file_txt.FileTxt()
        path_output = self.xml_config.get_output_path()
        txt_format.define_path(path_output + "\\")
        txt_format.create_txt_file(puzzle)

    def save_cvs(self, puzzle):
        """
           This method creates a puzzle in cvs format
           Keyword arguments:
                   puzzle : This variable has a sudoku game and save a cvs format
        """
        cvs_format_save = cvs_format.Cvs_format()
        path_output = self.xml_config.get_output_path()
        puzzle = cvs_format_save.change_to_cvs_format(puzzle)
        cvs_format_save.write_to_cvs_file(path_output, puzzle)

    def save_html(self,puzzle):
        """
           Keyword arguments:
                   puzzle : This variable has a sudoku game and save a html format
        """
        cvs_format_save = cvs_format.Cvs_format()
        path_output = self.xml_config.get_output_path()
        html_format = htmlsudoku.Htmlsudoku()
        html =  html_format.get_html(puzzle)
        html_format.html_to_file(html,path_output)

    def save_default(self):
        """
        This method save original and result puzzle in the format sppecified in the configuration
        file.
        Keyword arguments:
           puzzle : This variable has a sudoku game and save to format specified in config.xml
        """
        puzzle = self.get_original_sudoku()
        result = self.get_solved_puzzle()
        path_output = self.xml_config.get_output_path()
        default_format = self.xml_config.get_solver_output_type()
        if(default_format == "txt"):
           txt_format = file_txt.FileTxt()
           txt_format.define_path(path_output + "\\")
           print self.get_solved_puzzle()
           txt_format.create_txt_file(puzzle, result)
        elif default_format == "cvs":
           cvs_format_save = cvs_format.Cvs_format()
           path_output = self.xml_config.get_output_path()
           puzzle = cvs_format_save.change_to_cvs_format(puzzle)
           result = cvs_format_save.change_to_cvs_format(result)
           cvs_format_save.write_to_cvs_file(path_output, puzzle, result)
        elif default_format == "html":
           path_output = self.xml_config.get_output_path()
           html_format = htmlsudoku.Htmlsudoku()
           html =  html_format.get_html(puzzle, result)
           html_format.html_to_file(html,path_output)
        else:
             return "Format not supported"

    def get_solution(self,puzzle):
        """
        This method gets the solution of puzzle using the algorithm specified in the config.xml file
        Keyword arguments:
            Puzzle has a puzzle game and return the solution
        """
        algorithm = self.xml_config.get_algorithm_to_solve()
        if algorithm == "recursive":
           algorithm_recursive = recursive.Recursive(puzzle)
           self.puzzle_solved = algorithm_recursive.solve_one_sudoku()

        elif algorithm == "backtracking":
             algorithm_backtracking = resolve.Resolve(puzzle)
             matrix = algorithm_backtracking.convert_str_to_matrix(puzzle, 9, 9)
             algorithm_backtracking.resolve(matrix)
             self.puzzle_solved = algorithm_backtracking.get_solve_game()

        elif algorithm == "PeterNovig":
             algorithm_novig = peter_algorithm.PeterAlgorithm()
             self.puzzle_solved = algorithm_novig.get_game_solution(puzzle)
        else:
             return "Algorithm does not supported"

        return self.puzzle_solved

    def read_txt_file(self, path_file):
        """
        This method read a sudoku from a txt file
        Keyword arguments:
        path_file has the path of txt with sudoku
        """
        txt_file = file_txt.FileTxt()
        txt_file.define_path(path_file)
        self.puzzle_solved = ""
        txt_file.read_txt_file()
        self.puzzle_original = txt_file.parse_txt_file_on_a_single_line()
        self.puzzle_solved = self.get_solution(self.puzzle_original)
        print self.puzzle_solved
        return self.puzzle_original

    def read_cvs_file(self, path_file):
        """
        This method read a sudoku from a txt file
        Keyword arguments:
        path_file has the path of txt with sudoku
        """
        self.puzzle_solved = ""
        cvs_file = cvs_format.Cvs_format()
        cvs_file.read_a_cvs_form_file(path_file)
        if cvs_file.validate_sudoku_cvs():
           self.puzzle_original = cvs_file.get_sudoku_cvs_to_str()
           self.puzzle_solved = self.get_solution(self.puzzle_original)
           return self.get_original_sudoku()
        else:
           return []

