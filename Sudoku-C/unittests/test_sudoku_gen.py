import sys
sys.path.append("../lib")
import unittest
import sudoku

class Test_sudoku_gen(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_puzzle_array(self):
        board = []
        puzzle = sudoku.Sudoku()
        puzzle.get_sudoku(50,60)
        board = puzzle.get_puzzle_array()
        self.assertNotEqual([],board)

    def test_get_solution_array(self):
        board = []
        puzzle = sudoku.Sudoku()
        puzzle.get_sudoku(50,60)
        board = puzzle.get_solution_array()
        self.assertNotEqual([],board)

    def test_get_solution_str(self):
        puzzle = sudoku.Sudoku()
        puzzle.get_sudoku(50,60)
        board = puzzle.get_solution_str()
        self.assertNotEqual(0,puzzle.get_number_of_zeros())

    def test_get_number_of_zeros(self):
        puzzle = sudoku.Sudoku()
        puzzle.get_sudoku(61,61)
        board = puzzle.get_puzzle_srt()
        self.assertEqual(board.count("0"),puzzle.get_number_of_zeros())

    def test_get_verify_number_of_zeros_45(self):
        puzzle = sudoku.Sudoku()
        puzzle.get_sudoku(45,45)
        board = puzzle.get_puzzle_srt()
        self.assertEqual(45,puzzle.get_number_of_zeros())

    def test_get_verify_number_of_zeros_52(self):
        puzzle = sudoku.Sudoku()
        puzzle.get_sudoku(52,52)
        board = puzzle.get_puzzle_srt()
        self.assertEqual(52,puzzle.get_number_of_zeros())

    def test_get_verify_number_of_zeros_62(self):
        puzzle = sudoku.Sudoku()
        puzzle.get_sudoku(62,62)
        board = puzzle.get_puzzle_srt()
        self.assertEqual(62,puzzle.get_number_of_zeros())

    def test_get_verify_number_of_zeros_70(self):
        puzzle = sudoku.Sudoku()
        puzzle.get_sudoku(70,70)
        board = puzzle.get_puzzle_srt()
        self.assertEqual(70,puzzle.get_number_of_zeros())


    def test_get_verify_number_of_zeros_out_of_range(self):
        puzzle = sudoku.Sudoku()
        board = puzzle.get_sudoku(5,5)
        self.assertEqual("None",board)

#if __name__ == '__main__':
#    unittest.main()
