import unittest
import configuration
import os


class UnitTestConfiguration(unittest.TestCase):

    def setUp(self):

        self.xml_conf = configuration.Configuration()
        self.path_conf = self.xml_conf.get_configuration_path()

        self.xmlfile = configuration.Configuration("config.xml")
        self.xml_file_not_filled_fields = configuration.Configuration("config_NOT_filled_fields.xml")
        self.xml_file_with_filled_fields = configuration.Configuration("config_WITH_filled_fields.xml")

        self.root = self.xmlfile.read_xml(self.path_conf)
        self.root_NOT_fields = self.xml_file_not_filled_fields.read_xml(self.xml_file_not_filled_fields)
        self.root_WITH_fields = self.xml_file_with_filled_fields.read_xml(self.xml_file_with_filled_fields)

    def test_verify_if_config_file_exist_True(self):
        name = "config.xml"
        xml_conf = configuration.Configuration(name)
        self.assertTrue (xml_conf.verify_if_config_file_exist())

    def test_verify_if_config_file_exist_False(self):
        name = "config_false.xml"
        xml_conf = configuration.Configuration(name)
        self.assertFalse(xml_conf.verify_if_config_file_exist())

    def test_verify_if_config_file_exist_True_default(self):
        xml_conf = configuration.Configuration()
        file_path = xml_conf.get_configuration_path()
        xml_conf.create_default_configuration_xml(file_path)

        self.assertTrue(xml_conf.verify_if_config_file_exist())

    def test_verify_xml_format(self):
        xml_conf = configuration.Configuration()
        self.assertFalse(xml_conf.verify_xml_format())

    def test_create_default_configuration_xml_if_conf_file_does_not_exist(self):
        name = "config69.xml"
        xml_conf = configuration.Configuration(name)
        file_path = os.getcwd() + "\\configurations\\"+name
        xml_conf.create_default_configuration_xml(file_path)
        self.assertTrue(os.path.exists (file_path))

    def test_verify_if_modify_algorithm_node_in_xml(self):
        self.assertTrue(self.xml_conf.verify_modif_tag("algorithm", "backtraking"))

    def test_verify_if_modify_difficulty_node_in_xml(self):
        self.assertTrue(self.xml_conf.verify_modif_tag("difficulty", "Easy"))

    def test_verify_if_modify_solver_output_type_node_in_xml(self):
        self.assertTrue(self.xml_conf.verify_modif_tag("solver_output_type", "cvs"))

    def test_verify_if_modify_solver_path_output_type_node_in_xml(self):
        self.assertTrue(self.xml_conf.verify_modif_tag("path_output", "c:\\\\temp002"))

    def test_read_config_verify_config_file_has_not_ATRIBUTE_NAME_of_DEFAULT_TAG_it_should_take_the_default_NAME(self):
        self.assertEqual("configuration", self.xmlfile.get_name(self.root_NOT_fields))

    def test_read_config_verify_config_file_has_not_ALGORITHM_it_should_take_the_default_ALGORITHM_Backtraking(self):
        self.assertEqual("Backtraking", self.xmlfile.get_algorithm(self.root_NOT_fields))

    def test_read_config_verify_config_file_has_not_DIFFICULTY_it_should_take_the_default_DIFFICULTY_Easy(self):
        self.assertEqual("Easy", self.xmlfile.get_difficulty(self.root_NOT_fields))

    def test_read_config_verify_config_file_has_not_SOLVER_OUTPUT_TYPE_it_should_take_the_default_SOLVER_OUTPUT_TYPE_Txt(self):
        self.assertEqual("txt", self.xmlfile.get_solver_output_type(self.root_NOT_fields))

    def test_read_config_verify_config_file_has_not_PATH_it_should_take_the_default_PATH(self):
        var_path = "L:\\workspace\\Sudoku-v1\\Sudokuv1\\outputs\\"
        self.assertNotEqual(var_path, self.xmlfile.get_path_output(self.root_NOT_fields))


    def test_read_config_verify_config_file_can_read_the_ATRIBUTE_NAME_of_DEFAULT_TAG_it_should_be_attribute_name(self):
        self.assertEqual("configuration from file", self.xmlfile.get_name(self.root_WITH_fields))

    def test_read_config_verify_config_file_can_read_the_ALGORITHM_tag(self):
        self.assertEqual("Peter from xml", self.xmlfile.get_algorithm(self.root_WITH_fields))

    def test_read_config_verify_config_file_can_read_the_DIFFICULTY_tag(self):
        self.assertEqual("Hard from xml", self.xmlfile.get_difficulty(self.root_WITH_fields))

    def test_read_config_verify_config_file_can_read_SOLVER_OUTPUT_TYPE_tag(self):
        self.assertEqual("txt from xml", self.xmlfile.get_solver_output_type(self.root_WITH_fields))

    def test_read_config_verify_config_can_read_PATH_tag(self):
        self.assertEqual("path-from-xml", self.xmlfile.get_path_output(self.root_WITH_fields))



if __name__ == '__main__':
    unittest.main()
