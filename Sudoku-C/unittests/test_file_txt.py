import sys
sys.path.append("../lib")
import unittest
from file_txt import FileTxt

class TestFileTxt(unittest.TestCase):
    def setUp(self):
        self.path_of_the_file = "sources\\easyconretorno.txt"
        self.content_no_parsed = "040000700\n000700001\n005021006\n000800900\n600002003\n030005008\n301640000\n000050000\n006008200\n"
        self.content_parsed = "040000700000700001005021006000800900600002003030005008301640000000050000006008200"
        self.content_parsed_with_letter = "0400007000007000010050210060008009006m0002003030005008301640000000050000006008200"

        self.path_of_the_file_82_characteres = "sources\\easyconretorno82.txt"
        self.content_with_82_characteres = "040000700\n000700001\n005021006\n000800900\n6001002003\n030005008\n301640000\n000050000\n006008200"
        self.content_with_82_characteres_parsed = "0400007000007000010050210060008009006001002003030005008301640000000050000006008200"

        self.path_of_the_file_82_characteres = "sources\\easyconretornoletter.txt"
        self.content_parsed_with_letter = "0400007000007000010050210060008009006m0002003030005008301640000000050000006008200"

    def test_verify_define_path_returns_a_path(self):
        self.new_instance = FileTxt()
        path = self.new_instance.define_path (self.path_of_the_file)
        path_to_compare = "sources\\easyconretorno.txt"
        self.assertEqual (path_to_compare, path)

    def test_verify_the_function_read_txt_file_returns_a_game_in_form_of_9_characters_and_space(self):
        self.new_instance = FileTxt()
        self.new_instance.define_path (self.path_of_the_file)
        content_to_compare = self.new_instance.read_txt_file()
        self.assertEqual (self.content_no_parsed, content_to_compare)

    def test_verify_the_function_parse_txt_file_on_a_single_line_returns_a_game_parsed (self):
        self.new_instance = FileTxt()
        self.new_instance.define_path (self.path_of_the_file)
        self.new_instance.read_txt_file()
        content_to_compare = self.new_instance.parse_txt_file_on_a_single_line()
        self.assertEqual (self.content_parsed, content_to_compare)

    def test_verify_the_function_parse_txt_file_on_a_single_line_returns_a_false_when_the_game_has_greater_than_81_characteres (self):
        self.new_instance = FileTxt()
        self.new_instance.define_path (self.path_of_the_file_82_characteres)
        self.new_instance.read_txt_file()
        characteres = self.new_instance.parse_txt_file_on_a_single_line()
        self.assertFalse (characteres)

    def test_verify_the_function_parse_txt_file_on_a_single_line_returns_a_false_when_the_game_has_letters (self):
        self.new_instance = FileTxt()
        self.new_instance.define_path (self.path_of_the_file_82_characteres)
        self.new_instance.read_txt_file()
        characteres = self.new_instance.parse_txt_file_on_a_single_line()
        self.assertFalse (characteres)

    def test_verify_the_function_create_txt_file_creates_a_text_file (self):
        self.new_instance = FileTxt()
        self.new_instance.define_path("..\\outputs\\")
        file = self.new_instance.create_txt_file(self.content_parsed)
        self.assertTrue (file)

    def test_verify_the_function_get_quantity_of_zeros_returns_the_number_of_zeros_that_has_the_game (self):
        self.new_instance = FileTxt()
        quantity_of_zeros = self.new_instance.get_quantity_of_zeros(self.content_parsed)
        self.assertEqual (57, quantity_of_zeros)

    def test_verify_the_content_parsed_has_81_charateres (self):
        self.new_instance = FileTxt()
        characteres = self.new_instance.get_number_of_characters(self.content_parsed)
        self.assertTrue (characteres)

    def test_verify_the_content_parsed_has_greater_than_81_charateres (self):
        self.new_instance = FileTxt()
        characteres = self.new_instance.get_number_of_characters(self.content_with_82_characteres_parsed)
        self.assertFalse (characteres)

    def test_verify_the_content_are_only_digits (self):
        self.new_instance = FileTxt()
        digits = self.new_instance.get_if_is_digit (self.content_parsed)
        self.assertTrue (digits)

    def test_verify_when_the_content_not_only_has_digits_returns_a_false_value (self):
        self.new_instance = FileTxt()
        content_with_letter = self.new_instance.get_if_is_digit (self.content_parsed_with_letter)
        self.assertFalse(content_with_letter)

    def test_verify_the_function_create_txt_file_creates_a_text_file_same_format(self):
        self.new_instance = FileTxt()
        self.new_instance.define_path("..\\outputs\\")
        file = self.new_instance.create_txt_file(self.content_no_parsed, "salida")
        self.assertTrue (file)

#if __name__ == '__main__':
#	unittest.main()
