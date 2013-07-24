import os
import xml.etree.ElementTree as xmltree

class Menus:
    def __init__(self):
        """
        This method is the constructor
        """
        self.main_menu = ""
        self.sub_menu_game = ""
        self.sub_menu_options = ""
        self.sub_menu_read = ""
        self.sub_menu_save = ""
        self.sub_menu_algorithm = ""
        self.sub_menu_difficulty = ""
        self.sub_menu_difficulty_edith = ""
        self.path_of_file = os.getcwd() + "\\configurations\\"

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
        This method read a optiom from menu
        """
        lista = ""
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

    def set_main_menu(self, main_menu):
        """
        This method read a optiom from menu
        """
        if main_menu == "g":
            self.main_menu = "Game"
        elif main_menu == "o":
            self.main_menu = "Option"
        elif main_menu == "x":
            self.main_menu = "Exit"
        else:
            self.main_menu = "choose another option"

    def set_sub_menu_game(self, sub_menu_game):
        """
        This method read a optiom from sub-menu
        """
        if sub_menu_game == "p":
            self.sub_menu_game = "Play"
        elif sub_menu_game == "g":
            self.sub_menu_game = "Generate"
        elif sub_menu_game == "l":
            self.sub_menu_game = "Resolve"
        elif sub_menu_game == "r":
            self.sub_menu_game = "Read"
        elif sub_menu_game == "s":
            self.sub_menu_game = "Save"
        elif sub_menu_game == "t":
            self.sub_menu_game = "Reset"
        elif sub_menu_game == "b":
            self.sub_menu_game = "Back"
        else:
            self.sub_menu_game = "Please choose another option"

    def set_sub_menu_read(self, sub_menu_read):
        """
        This method read a optiom from menu
        """
        if sub_menu_read == "t":
            self.sub_menu_read = "txt"
        elif sub_menu_read == "c":
            self.sub_menu_read = "csv"
        elif sub_menu_read == "b":
            self.sub_menu_read = "Back"
        else:
            self.sub_menu_read = "Please choose another option"

    def set_sub_menu_save(self, sub_menu_save):
        """
        This method read a optiom from menu
        """
        if sub_menu_save == "t":
            self.sub_menu_save = "txt"
        elif sub_menu_save == "c":
            self.sub_menu_save = "csv"
        elif sub_menu_save == "h":
            self.sub_menu_save = "html"
        elif sub_menu_save == "d":
            self.sub_menu_save = "default (solved)"
        elif sub_menu_save == "b":
            self.sub_menu_save = "Back"
        else:
            self.sub_menu_save = "Please choose another option"

    def set_sub_menu_options(self, sub_menu_options):
        """
        This method read a optiom from menu
        """
        if sub_menu_options == "a":
            self.sub_menu_options = "Algorithm"
        elif sub_menu_options == "d":
            self.sub_menu_options = "Difficulty"
        elif sub_menu_options == "v":
            self.sub_menu_options = "Solver_out_put"
        elif sub_menu_options == "b":
            self.sub_menu_options = "Back"
        else:
            self.sub_menu_options = "Please choose another option"

    def set_sub_menu_algorithm(self, sub_menu_algorithm):
        """
        This method read a optiom from menu
        """
        if sub_menu_algorithm == "k":
            self.sub_menu_algorithm = "Backtrack"
        elif sub_menu_algorithm == "n":
            self.sub_menu_algorithm = "Peter Norwick"
        elif sub_menu_algorithm == "i":
            self.sub_menu_algorithm = "Recursive"
        elif sub_menu_algorithm == "b":
            self.sub_menu_algorithm = "Back"
        else:
            self.sub_menu_algorithm = "Please choose another option"

    def set_sub_menu_difficulty(self, sub_menu_difficulty):
        """
        This method read a optiom from menu
        """
        if sub_menu_difficulty == "e":
            self.sub_menu_difficulty = "Easy"
        elif sub_menu_difficulty == "m":
            self.sub_menu_difficulty = "Medium"
        elif sub_menu_difficulty == "a":
            self.sub_menu_difficulty = "Hard"
        elif sub_menu_difficulty == "b":
            self.sub_menu_difficulty = "Back"
        else:
            self.sub_menu_difficulty = "Please choose another option"

    def set_sub_menu_difficulty_edith(self, sub_menu_difficulty_edith):
        """
        This method read a optiom from menu
        """
        if sub_menu_difficulty_edith == "nw":
            self.sub_menu_difficulty_edith = "New"
        elif sub_menu_difficulty_edith == "ch":
            self.sub_menu_difficulty_edith = "Change Values"
        elif sub_menu_difficulty_edith == "b":
            self.sub_menu_difficulty_edith = "Back"
        else:
            self.sub_menu_difficulty_edith = "Please choose another option"

    def get_main_menu(self):
        """
        This method return the main menu
        """
        return self.main_menu

    def get_sub_menu_game(self):
        """
        This method reurn a submenu
        """
        return self.sub_menu_game

    def get_sub_menu_read(self):
        """
        This method return the menu Read
        """
        return self.sub_menu_read

    def get_sub_menu_save(self):
        """
        This method return the menu Save
        """
        return self.sub_menu_save

    def get_sub_menu_options(self):
        """
        This method return the menu Options
        """
        return self.sub_menu_options

    def get_sub_menu_algorithm(self):
        """
        This method return the menu Algorithm
        """
        return self.sub_menu_algorithm

    def get_sub_menu_difficulty(self):
        """
        This method return the menu Difficulty
        """
        return self.sub_menu_difficulty

    def get_sub_menu_difficulty_edith(self):
        """
        This method return the menu difficulty Edit
        """
        return self.sub_menu_difficulty_edith

    def print_main_menu(self):
        """
        This method print in the console the main menu
        """
        print "----------------------------"
        print "        Main Menu           "
        print "----------------------------"
        print "(p) Play >", "     (x) Exit", "\n",
        print "(o) Options >"


    def print_sub_menu_game(self):
        """
        This method print in the console the game menu
        """
        print "(p) Play >", "   (s) Save ->", "\n",
        print "(g) Generate", " (t) Reset", "\n",
        print "(l) Resolve", "  (b) Back to Main Menu <-", "\n",
        print "(r) Read >"

    def print_sub_menu_play(self):
        """
        This method print in the console the play menu
        """
        print "(g) Generate", "(v) Solve ", " (q) Quit ", "\n",
        print "(r) Read>", "   (t) Reset ", "\n",
        print "(h) Hit", "     (s) Save>", "\n",
        self.set_tips()


    def set_tips(self):
        """
        This method print in the console the option to play a sudoku game
        """
        print "---------------------------------"
        print 'Introduce your game like: AB5'
        print "A -> row, B -> column, 5 -> value"
        print "---------------------------------"

    def print_sub_menu_read(self):
        """
        This method print in the console the read menu
        """
        print "----------------------------"
        print "   How to load the Game   "
        print "----------------------------"
        print "(t) Txt", "     (c) Console ", "\n",
        print "(v) CSV", "     (b) Back to Game menu <"

    def print_sub_menu_save(self):
        """
        This method print in the console the save menu
        """
        print "--------------"
        print "Sub Menu Save"
        print "-------------"
        print "(t) Txt", "  (d) default [solved]", "\n",
        print "(c) CSV", "  (b) Back to Game Menu <", "\n",
        print "(h) html", "\n",

    def print_sub_menu_options(self):
        """
        This method print in the console the option menu
        """
        print "----------------------------"
        print "       Sub Menu options"
        print "----------------------------"
        print "(a) Algorithm >", "  (v) Solved out put", "\n",
        print "(d) Difficulty >", " (b) Back to Main Menu <", "\n",

    def print_sub_menu_algorithm(self):
        """
        This method print in the console the algorithm menu
        """
        print "----------------------------"
        print "     Sub Menu Algorithm"
        print "----------------------------"
        print "(k) Backtrack", "     (i) Recursive", "\n",
        print "(n) Peter Norwick", " (b) Back to Option Menu <", "\n",

    def print_sub_menu_difficulty(self):
        """
        This method print in the console the difficulty menu
        """
        print "(e) Edit >", "(b) Back to Option Menu <", "\n",

    def get_difficulty_matrix(self):
        """
        Return a difficulty levels
        """
        return self.get_difficulty_levels(self.read_xml("config.xml"))

    def print_list_difficulty(self):
        """
        This method print in the console the difficulty menu
        """
        print "----------------------------"
        print "     Sub Menu Difficulty    "
        print "----------------------------"
        difficulty_matrix = self.get_difficulty_matrix()
        rows = len (difficulty_matrix)

        for row in range(rows):
            print "(%s) %s" %(difficulty_matrix[row][0], difficulty_matrix[row][1])

    def print_sub_menu_solved_out_put(self):
        """
        This method print in the console the solve menu
        """
        print "----------------------------"
        print "  Sub Menu Solved out put   "
        print "----------------------------"
        print "(t) Txt", " (h) html", "\n",
        print "(c) CSV", " (b) Back to Option Menu <", "\n",

    def print_sub_menu_edit(self):
        """
        This method print in the console the edit menu
        """
        print "(n) New", "         (b) Back to Difficulty menu <", "\n",
        print "(c) Change value"



