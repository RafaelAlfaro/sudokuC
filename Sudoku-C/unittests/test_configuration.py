import sys
sys.path.append("../lib")
import unittest
import configuration
import os

class TestConfiguration(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_folders_are_not_exist():
        name = "config.xml"
        xml_conf = configuration.Configuration()
        value = xml_conf.create_folders_are_not_exist()
        self.assertTrue(value)

    def test_modify_path_conf_file(self):
        name = "config.xml"
        xml_conf = configuration.Configuration()
        xml_conf.modify_path_conf_file("..\\modify\\")
        value = xml_conf.get_configuration_path()
        self.assertEqual("..\\modify\\config.xml", value)

    def test_verify_if_config_file_exist_True(self):
        name = "config.xml"
        xml_conf = configuration.Configuration()
        xml_conf = configuration.Configuration(name)
        exist = xml_conf.verify_if_config_file_exist()
        self.assertTrue (exist)

    def test_verify_if_config_file_exist_False(self):
        name = "config_false.xml"
        xml_conf = configuration.Configuration(name)
        self.assertFalse(xml_conf.verify_if_config_file_exist())
##
    def test_verify_if_config_file_exist_True_default(self):
        xml_conf = configuration.Configuration()
        file_path = xml_conf.get_configuration_path()
        xml_conf.create_default_configuration_xml(file_path)
        self.assertTrue(xml_conf.verify_if_config_file_exist())

    def test_verify_xml_format(self):
        xml_conf = configuration.Configuration()
        self.assertFalse(xml_conf.verify_xml_format())
##
    def test_create_default_configuration_xml_if_conf_file_does_not_exist(self):
        name = "config69.xml"
        xml_conf = configuration.Configuration(name)
##        file_path = os.getcwd() + "..\\configurations\\"+name
        file_path = "sources\\"+name
        xml_conf.create_default_configuration_xml(file_path)
        self.assertTrue(os.path.exists (file_path))

    def test_verify_if_modify_algorithm_node_in_xml(self):
        name = "config.xml"
        xml_conf = configuration.Configuration(name)
        file_modify = xml_conf.verify_modif_tag("algorithm", "backtraking")
        self.assertTrue(file_modify)
##
    def test_verify_if_modify_difficulty_node_in_xml(self):
        name = "config.xml"
        xml_conf = configuration.Configuration(name)
        file_modify = xml_conf.verify_modif_tag("difficulty", "Easy")
        self.assertTrue(file_modify)

    def test_verify_if_modify_solver_output_type_node_in_xml(self):
        name = "config.xml"
        xml_conf = configuration.Configuration(name)
        file_modify = xml_conf.verify_modif_tag("solver_output_type", "cvs")
        self.assertTrue(file_modify)

    def test_verify_if_modify_solver_path_output_type_node_in_xml(self):
        name = "config.xml"
        xml_conf = configuration.Configuration(name)
        file_modify = xml_conf.verify_modif_tag("path_output", "c:\\\\temp002")
        self.assertTrue(file_modify)

    def test_get_number_of_levels(self):
        name = "config.xml"
        xml_conf = configuration.Configuration(name)
        value = xml_conf.get_number_of_levels()
        self.assertLess(0,value)

    def test_modify_levels(self):
        name = "config.xml"
        xml_conf = configuration.Configuration(name)
        level = 'Easy'
        min_zeros = 45
        max_zeros = 52
        value = xml_conf.modify_levels(level, min_zeros, max_zeros)
        self.assertTrue(value)

    def test_add_levels(self):
        name = "config.xml"
        xml_conf = configuration.Configuration(name)
        level = 'New level'
        min_zeros = 45
        max_zeros = 52
        value_before = xml_conf.get_number_of_levels()
        levels = xml_conf.add_levels(level, min_zeros, max_zeros)
        value_after = xml_conf.get_number_of_levels()
        self.assertNotEqual(value_after,value_before)

    def test_read_config_verify_config_file_can_read_the_ALGORITHM_tag(self):
        value = ""
        xmlfile = configuration.Configuration("config.xml")
        path_conf = xmlfile.get_configuration_path()
        root = xmlfile.read_xml(path_conf)
        value = xmlfile.get_value_from_xml(root,'algorithm')
        self.assertNotEqual("", value)

    def test_read_config_verify_config_file_can_read_the_DIFFICULTY_tag(self):
        value = ""
        xmlfile = configuration.Configuration("config.xml")
        path_conf = xmlfile.get_configuration_path()
        root = xmlfile.read_xml(path_conf)
        value = xmlfile.get_value_from_xml(root,'difficulty')
        self.assertNotEqual("", value)

    def test_read_config_verify_config_file_can_read_SOLVER_OUTPUT_TYPE_tag(self):
        value = ""
        xmlfile = configuration.Configuration("config.xml")
        path_conf = xmlfile.get_configuration_path()
        root = xmlfile.read_xml(path_conf)
        value = xmlfile.get_value_from_xml(root,'solver_output_type')
        self.assertNotEqual("", value)

    def test_read_config_verify_config_can_read_PATH_tag(self):
        value = ""
        xmlfile = configuration.Configuration("config.xml")
        path_conf = xmlfile.get_configuration_path()
        root = xmlfile.read_xml(path_conf)
        value = xmlfile.get_value_from_xml(root,'path_output')
        self.assertNotEqual("", value)

    def test_create_folder_of_configuration (self):
        value = ""
        path = "sources\\conf_alt"
        xmlfile = configuration.Configuration("config.xml")
        xmlfile.modify_path_conf_file(path)
        if (os.path.exists(path)):
            os.removedirs(path)
            print ("Removed")
        self.assertTrue(xmlfile.create_folders_are_not_exist())

    def test_create_folder_output(self):
        value = ""
        xmlfile = configuration.Configuration()
        path = "sources\\output"
        xmlfile.modify_path_output(path)
        if (os.path.exists(path)):
            os.removedirs(path)
            print ("Removed")
        self.assertTrue(xmlfile.create_folders_are_not_exist())


#if __name__ == '__main__':
#    unittest.main()
