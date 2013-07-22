import sys
sys.path.append("../lib")

import unittest
import htmlsudoku

class Test_Htmlsudoku(unittest.TestCase):

    def setUp(self):
        self.board_colors = ["FFFFFF","FF8AD8","F592FF","E6FF92","95FF92","BFCDD5","92FFCE","92D2FF","92A0FF","BC92FF"]

    def test_get_board_color(self):
        html = htmlsudoku.Htmlsudoku()
        cells = [11,14,17,37,40,43,64,67,70]
        color_out = ["FFFFFF"]
        for cell in cells:
            color_out.append(html.get_board_color(cell))
        self.assertEqual(self.board_colors,color_out)

    def test_mofify_header(self):
        html = htmlsudoku.Htmlsudoku()
        str_to_verify = "<html>\n<head>\n<title>test</title>\n</head>\n"
        self.assertEqual(str_to_verify,html.mofify_header("test"))

    def test_modify_table_header(self):
         html = htmlsudoku.Htmlsudoku()
         str_to_verify = "<table summary=\"value\" border=color align=\"center\">\n<caption>value</caption>\n"
         self.assertEqual(str_to_verify,html.modify_table_header("value","color"))

    def test_modify_th_column(self):
        html = htmlsudoku.Htmlsudoku()
        str_to_verify = "<th scope=\"col\" bgcolor=#color width= 10 align= \"center\">value</th>\n"
        self.assertEqual(str_to_verify,html.modify_th_column("color","value"))

    def test_make_columns(self):
        html = htmlsudoku.Htmlsudoku()
        chars = len(html.make_columns())
        self.assertLessEqual(20,chars)

    def test_generate_table(self):
        puzzle = "040000700000700001005021006000800900600002003030005008301640000000050000006008200"
        html = htmlsudoku.Htmlsudoku()
        chars = len(html.generate_table(puzzle))
        self.assertLessEqual(20,chars)

    def test_make_table(self):
        puzzle = "040000700000700001005021006000800900600002003030005008301640000000050000006008200"
        html = htmlsudoku.Htmlsudoku()
        htmt_out =  html.make_table(puzzle,"Title")
        self.assertEqual(2,htmt_out.count("Title"))

    def test_get_html_without_result(self):
        puzzle = "040000700000700001005021006000800900600002003030005008301640000000050000006008200"
        html = htmlsudoku.Htmlsudoku()
        html_generated =  html.get_html(puzzle)
        self.assertLessEqual(20,len(html_generated))

    def test_get_html_with_result(self):
        puzzle = "040000700000700001005021006000800900600002003030005008301640000000050000006008200"
        result = "340600000007000000020080570000005000070010020000400000036020010000000900000007082"
        html = htmlsudoku.Htmlsudoku()
        html_generated =  html.get_html(puzzle,result)
        self.assertLessEqual(20,len(html_generated))


    def test_generate_name(self):
        html = htmlsudoku.Htmlsudoku()
        file_name = html.generate_name()
        self.assertLessEqual(1,file_name.count("sudoku_"))


    def test_generate_name_name(self):
        html = htmlsudoku.Htmlsudoku()
        file_name = html.generate_name("Test")
        print(file_name)
        self.assertLessEqual(1,file_name.count("Test_"))

    def test_html_to_file(self):
        puzzle = "040000700000700001005021006000800900600002003030005008301640000000050000006008200"
        result = "340600000007000000020080570000005000070010020000400000036020010000000900000007082"
        path_file = "..\\outputs"
        html = htmlsudoku.Htmlsudoku()
        result = html.html_to_file(html.get_html(puzzle,result),path_file)

    def test_html_to_file_error(self):
        puzzle = "040000700000700001005021006000800900600002003030005008301640000000050000006008200"
        result = "340600000007000000020080570000005000070010020000400000036020010000000900000007082"
        path_file = "c:\\temp_false\\test.html"
        html = htmlsudoku.Htmlsudoku()
        result = html.html_to_file(html.get_html(puzzle,result),path_file)
        self.assertEqual("The file cannot be written",result)


if __name__ == '__main__':
    unittest.main()
