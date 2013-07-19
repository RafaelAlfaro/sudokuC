import sys
sys.path.append("../lib")

import unittest
import os
import cvs_format

class Test_cvs_format(unittest.TestCase):

    def setUp(self):
        #valida sudoku
        self.cvs_sk="040000700,000700001,005021006,000800900,600002003,030005008,301640000,000050000,006008200"
        #not valid sudoku
        self.cvs_not_sk="040000700,000700001,005021006,0008009,600002003,030005008,301640000,000050000,006008200"
        #sudoku in str
        self.sk_str = "040000700000700001005021006000800900600002003030005008301640000000050000006008200"
        self.sk_cvs_in_file = "340600000,007000000,020080570,000005000,070010020,000400000,036020010,000000900,000007082"
        self.sk_str_dots = ".4....7.....7....1..5.21..6...8..9..6....2..3.3...5..83.164........5......6..82.."
        self.path = os.getcwd()
        self.cvs_path = self.path + "\\sources\\cvs_file_1.cvs"
        self.cvs_path_save = self.path + "\\sources\\cvs_file_2.cvs"
        self.multilines_cvs = self.path + "\\sources\\multi_line_cvs.cvs"
        self.false_path = self.path + "\\sources\\not_file.cvs"

    def test_get_lines_from_a_cvs_file(self):
        cvs_validation = cvs_format.Cvs_format()
        lines = cvs_validation.get_lines_cvs_file(self.multilines_cvs)
        sk_cmp = self.cvs_sk + '\n'
        last_line = lines[len(lines)-1]
        self.assertEqual(sk_cmp,last_line)


    def test_get_lines_from_a_cvs_false_file(self):
        cvs_validation = cvs_format.Cvs_format()
        lines = cvs_validation.get_lines_cvs_file(self.false_path)
        error_file = "The file cannot be read"
        self.assertEqual(error_file, lines)



    def test_read_a_cvs_form_file(self):
        cvs_validation = cvs_format.Cvs_format()
        cvs_validation.read_a_cvs_form_file(self.cvs_path)
        cvs_puzzle = cvs_validation.get_sudoku_cvs()
        self.assertEqual(self.sk_cvs_in_file,cvs_puzzle)

    def test_write_to_cvs_file(self):
        cvs_validation = cvs_format.Cvs_format()
        cvs_validation.write_to_cvs_file(self.cvs_path_save,self.sk_cvs_in_file)
        cvs_validation.read_a_cvs_form_file(self.cvs_path_save)
        cvs_puzzle = cvs_validation.get_sudoku_cvs()
        self.assertEqual(self.sk_cvs_in_file,cvs_puzzle)

    def test_get_sudoku_cvs(self):
        cvs_validation = cvs_format.Cvs_format(self.cvs_sk)
        self.assertEqual(self.cvs_sk, cvs_validation.get_sudoku_cvs())

    def test_put_sudoku_cvs(self):
        cvs_validation = cvs_format.Cvs_format()
        empty = cvs_validation.get_sudoku_cvs()
        cvs_validation.put_sudoku_cvs(self.cvs_sk)
        self.assertNotEqual(empty, cvs_validation.get_sudoku_cvs())

    def test_verify_commas_True(self):
        cvs_validation = cvs_format.Cvs_format(self.cvs_sk)
        self.assertTrue(cvs_validation.verify_commas())

    def test_verify_commas_False(self):
        cvs_validation = cvs_format.Cvs_format(self.cvs_not_sk)
        self.assertFalse(cvs_validation.verify_commas())

    def test_validate_sudoku_cvs_True(self):
        cvs_validation = cvs_format.Cvs_format(self.cvs_sk)
        self.assertTrue(cvs_validation.validate_sudoku_cvs())

    def test_validate_sudoku_cvs_False(self):
        cvs_validation = cvs_format.Cvs_format(self.cvs_not_sk)
        self.assertFalse(cvs_validation.validate_sudoku_cvs())

    def test_get_sudoku_cvs_to_str(self):
        cvs_validation = cvs_format.Cvs_format(self.cvs_sk)
        self.assertEqual(self.sk_str,cvs_validation.get_sudoku_cvs_to_str())

    def test_change_to_cvs_format(self):
        cvs_validation = cvs_format.Cvs_format()
        sk_str_changed = cvs_validation.change_to_cvs_format(self.sk_str_dots)
        self.assertEqual(self.sk_str, sk_str_changed)

    def test_get_sudoku_cvs_to_str_false(self):
        self.sk_str_dots = self.sk_str_dots + "A"
        cvs_validation = cvs_format.Cvs_format(self.sk_str_dots)
        value = cvs_validation.get_sudoku_cvs_to_str()
        self.assertEqual([], value)

    def test_read_a_cvs_form_file_false(self):
        path_false = "j:\\path_false\\false.cvs"
        cvs_validation = cvs_format.Cvs_format()
        value = cvs_validation.read_a_cvs_form_file(path_false)
        self.assertEqual("The file cannot be read", value)

    def test_write_to_cvs_file_false(self):
        path_false = "j:\\path_false\\false.cvs"
        cvs_validation = cvs_format.Cvs_format()
        value = cvs_validation.write_to_cvs_file(path_false,self.sk_str)
        self.assertEqual("The file cannot be read", value)

##if __name__ == '__main__':
##    sys.exit(unittest.main())
