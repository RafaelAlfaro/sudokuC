import sys
sys.path.append("../lib")
import unittest
from menus import Menus


class UnitTestMenus(unittest.TestCase):
    def setUp(self):
        self.new_menu = Menus()

    
    def test_menu_has_a_title(self):
        pass
    
    """ Main Menu """
    def test_main_menu_should_be_Game_while_main_menu_has_bee_set_g(self):
        self.new_menu.set_main_menu("g")
        self.assertEqual("Game", self.new_menu.get_main_menu())
        
    def test_main_menu_should_be_Option_while_main_menu_has_bee_set_o(self):
        self.new_menu.set_main_menu("o")
        self.assertEqual("Option", self.new_menu.get_main_menu())

    def test_main_menu_should_be_Exit_while_main_menu_has_bee_set_x(self):
        self.new_menu.set_main_menu("x")
        self.assertEqual("Exit", self.new_menu.get_main_menu())
        
    def test_main_menu_should_not_continue_to_different_option(self):
        self.new_menu.set_main_menu("a")
        self.assertEqual("choose another option", self.new_menu.get_main_menu())
    
    """ Sub Menu Game """
    def test_sub_menu_Game_should_be_Play_while_it_has_been_set_p(self):
        self.new_menu.set_sub_menu_game("p")
        self.assertEqual("Play", self.new_menu.get_sub_menu_game())

    def test_sub_menu_Game_should_be_Generate_while_it_has_been_set_g(self):
        self.new_menu.set_sub_menu_game("g")
        self.assertEqual("Generate", self.new_menu.get_sub_menu_game())
    
    def test_sub_menu_Game_should_be_Resolve_while_it_has_been_set_l(self):
        self.new_menu.set_sub_menu_game("l")
        self.assertEqual("Resolve", self.new_menu.get_sub_menu_game())
    
    def test_sub_menu_Game_should_be_Read_while_it_has_been_set_r(self):
        self.new_menu.set_sub_menu_game("r")
        self.assertEqual("Read", self.new_menu.get_sub_menu_game())
    
    def test_sub_menu_Game_should_be_Save_while_it_has_been_set_s(self):
        self.new_menu.set_sub_menu_game("s")
        self.assertEqual("Save", self.new_menu.get_sub_menu_game())
    
    def test_sub_menu_Game_should_be_Reset_while_it_has_been_set_t(self):
        self.new_menu.set_sub_menu_game("t")
        self.assertEqual("Reset", self.new_menu.get_sub_menu_game())

    def test_sub_menu_Game_should_be_Back_while_it_has_been_set_b(self):
        self.new_menu.set_sub_menu_game("b")
        self.assertEqual("Back", self.new_menu.get_sub_menu_game())
    
    def test_sub_menu_Game_should_not_continue_to_some_one_else_selection_higher_than_6(self):
        self.new_menu.set_sub_menu_game(7)
        self.assertEqual("choose another option", self.new_menu.get_sub_menu_game())
  
    def test_sub_menu_Game_should_not_continue_to_some_one_else_selection_lower_than_1(self):
        self.new_menu.set_sub_menu_game(-3)
        self.assertEqual("choose another option", self.new_menu.get_sub_menu_game())
        
    def test_sub_menu_Game_should_not_continue_to_different_option(self):
        self.new_menu.set_sub_menu_game("f")
        self.assertEqual("choose another option", self.new_menu.get_sub_menu_game())
    
    """ Sub Menu Read """
    def test_sub_menu_Read_should_be_Txt_while_it_has_been_set_t(self):
        self.new_menu.set_sub_menu_read("t")
        self.assertEqual("txt", self.new_menu.get_sub_menu_read())
    
    def test_sub_menu_Read_should_be_Csv_while_it_has_been_set_c(self):
        self.new_menu.set_sub_menu_read("c")
        self.assertEqual("csv", self.new_menu.get_sub_menu_read())
    
    def test_sub_menu_Read_should_be_Read_while_it_has_been_set_b(self):
        self.new_menu.set_sub_menu_read("b")
        self.assertEqual("Back", self.new_menu.get_sub_menu_read())
   
    def test_sub_menu_Read_should_not_continue_to_alphabetic_option(self):
        self.new_menu.set_sub_menu_read("f")
        self.assertEqual("choose another option", self.new_menu.get_sub_menu_read())
     
    
    """ Sub Menu Save """
    def test_sub_menu_Save_should_be_Txt_while_it_has_been_set_t(self):
        self.new_menu.set_sub_menu_save("t")
        self.assertEqual("txt", self.new_menu.get_sub_menu_save())
    
    def test_sub_menu_Save_should_be_Csv_while_it_has_been_set_c(self):
        self.new_menu.set_sub_menu_save("c")
        self.assertEqual("csv", self.new_menu.get_sub_menu_save())
    
    def test_sub_menu_Save_should_be_Html_while_it_has_been_set_h(self):
        self.new_menu.set_sub_menu_save("h")
        self.assertEqual("html", self.new_menu.get_sub_menu_save())
    
    def test_sub_menu_Save_should_be_Back_while_it_has_been_set_4(self):
        self.new_menu.set_sub_menu_save("b")
        self.assertEqual("Back", self.new_menu.get_sub_menu_save())
         
    def test_sub_menu_Save_should_not_continue_to_different_option(self):
        self.new_menu.set_sub_menu_save("a")
        self.assertEqual("choose another option", self.new_menu.get_sub_menu_save())
    
    """ Sub Menu Option """
    def test_sub_menu_Options_should_be_Algorithm_while_it_has_been_set_a(self):
        self.new_menu.set_sub_menu_options("a")
        self.assertEqual("Algorithm", self.new_menu.get_sub_menu_options())
    
    def test_sub_menu_Options_should_be_Difficulty_while_it_has_been_set_d(self):
        self.new_menu.set_sub_menu_options("d")
        self.assertEqual("Difficulty", self.new_menu.get_sub_menu_options())
    
    def test_sub_menu_Options_should_be_Solver_out_put_while_it_has_been_set_v(self):
        self.new_menu.set_sub_menu_options("v")
        self.assertEqual("Solver_out_put", self.new_menu.get_sub_menu_options())
    
    def test_sub_menu_Options_should_be_Back_while_it_has_been_set_b(self):
        self.new_menu.set_sub_menu_options("b")
        self.assertEqual("Back", self.new_menu.get_sub_menu_options())
    
    def test_sub_menu_Options_should_not_continue_to_alphabetic_option(self):
        self.new_menu.set_sub_menu_options("f")
        self.assertEqual("choose another option", self.new_menu.get_sub_menu_options())
    
    """ Sub Menu Algorithm"""
    def test_sub_menu_Algorithm_should_be_Backtrack_while_it_has_been_set_k(self):
        self.new_menu.set_sub_menu_algorithm("k")
        self.assertEqual("Backtrack", self.new_menu.get_sub_menu_algorithm())
    
    def test_sub_menu_Algorithm_should_be_Peter_while_it_has_been_set_n(self):
        self.new_menu.set_sub_menu_algorithm("n")
        self.assertEqual("Peter Norwick", self.new_menu.get_sub_menu_algorithm())
    
    def test_sub_menu_Algorithm_should_be_Recursive_out_put_while_it_has_been_set_i(self):
        self.new_menu.set_sub_menu_algorithm("i")
        self.assertEqual("Recursive", self.new_menu.get_sub_menu_algorithm())
    
    def test_sub_menu_Algorithm_should_be_Back_while_it_has_been_set_b(self):
        self.new_menu.set_sub_menu_algorithm("b")
        self.assertEqual("Back", self.new_menu.get_sub_menu_algorithm())
        
    def test_sub_menu_Algorithm_should_not_continue_to_different_option(self):
        self.new_menu.set_sub_menu_algorithm("f")
        self.assertEqual("choose another option", self.new_menu.get_sub_menu_algorithm())
        
    """ Sub Menu Difficulty """
    def test_sub_menu_difficulty_should_be_Easy_while_it_has_been_set_e(self):
        self.new_menu.set_sub_menu_difficulty("e")
        self.assertEqual("Easy", self.new_menu.get_sub_menu_difficulty())
    
    def test_sub_menu_difficulty_should_be_Medium_while_it_has_been_set_m(self):
        self.new_menu.set_sub_menu_difficulty("m")
        self.assertEqual("Medium", self.new_menu.get_sub_menu_difficulty())
    
    def test_sub_menu_difficulty_should_be_Hard_while_it_has_been_set_a(self):
        self.new_menu.set_sub_menu_difficulty("a")
        self.assertEqual("Hard", self.new_menu.get_sub_menu_difficulty())
    
    def test_sub_menu_difficulty_should_be_Back_while_it_has_been_set_b(self):
        self.new_menu.set_sub_menu_difficulty("b")
        self.assertEqual("Back", self.new_menu.get_sub_menu_difficulty())
         
    def test_sub_menu_difficulty_should_not_continue_to_alphabetic_option(self):
        self.new_menu.set_sub_menu_difficulty("f")
        self.assertEqual("choose another option", self.new_menu.get_sub_menu_difficulty())
    
    """ Sub Menu Difficulty Edith """
    def test_sub_menu_difficulty_edith_should_be_Easy_while_it_has_been_set_nw(self):
        self.new_menu.set_sub_menu_difficulty_edith("nw")
        self.assertEqual("New", self.new_menu.get_sub_menu_difficulty_edith())
    
    def test_sub_menu_difficulty_edith_should_be_Medium_while_it_has_been_set_ch(self):
        self.new_menu.set_sub_menu_difficulty_edith("ch")
        self.assertEqual("Change Values", self.new_menu.get_sub_menu_difficulty_edith())
    
    def test_sub_menu_difficulty_edith_should_be_Back_while_it_has_been_set_b(self):
        self.new_menu.set_sub_menu_difficulty_edith("b")
        self.assertEqual("Back", self.new_menu.get_sub_menu_difficulty_edith())
         
    def test_sub_menu_difficulty_edith_should_not_continue_to_alphabetic_option(self):
        self.new_menu.set_sub_menu_difficulty_edith("f")
        self.assertEqual("choose another option", self.new_menu.get_sub_menu_difficulty_edith())

    
if __name__ == '__main__':
    unittest.main()
