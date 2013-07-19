#-------------------------------------------------------------------------------
# Name:    Configuration
# Purpose: The purpose of this test case is handle a XML. This xml will be said config.xml
#          The config.xml contains the configration of Sudoku game:
#          algorithm : This atribute will contain the algorithm to be use by default.
#				Peter Novig
#				Backtraking
#               Recursive
#	difficulty : This atribute will contain the levels of difficulty
#				 Easy : TBD
#				 Medium : TBD
#				 Hard : TBD
#	solver_output_type : This attribute will contain output type
#								txt -
#	path_to_save : This attribute will contain the default path where the output file will be saved
#
# Author(s):
#           Carla Munoz <CM>
#           Gustavo Ramirez <GR>
#           Rafael Alfaro <RAM>
#
# Created:     01/07/2013
#-------------------------------------------------------------------------------
import os
import xml.etree.ElementTree as xmltree


class Configuration:
    def __init__(self, file_name = "config.xml"):
        """
        This method is the object constructor
        name - the variable "name" has the name of xml file, the default parameter is config.xml

        self.algorithm - Algorithm used
        self.difficulty - Difficulty used
        self.id - id of level
        self.min - minimums hold in the board
        self.max - Maximus hold in the board
        self.solver_output_type - type of output (txt or cvs)
        self.output_path - the path of output
        self.name = attribute of configuration tag
        """

        self.name_of_file = file_name
        self.path_of_file = "..\\configurations\\"
        self.algorithm = "Backtraking"
        self.difficulty = "Easy"
        self.id = "1"
        self.min = "46"
        self.max = "49"
        self.solver_output_type = "txt"
        self.output_path = "..\\outputs\\"
        self.name = "configuration"

##    def print_configuration (self):
##        """
##        This method prints the variables of object
##        algorithm - Algorithm used
##        difficulty - Difficulty used
##        id - id of level
##        min - minimums hold in the board
##        max - Maximus hold in the board
##        solver_output_type - type of output (txt or cvs)
##        output_path - the path of output
##
##        """
##        print("Name : ", self.name_of_file)
##        print("Path of scrypt :", self.path_of_file)
##        print("Algorithm:", self.algorithm)
##        print("Difficulty:", self.difficulty)
##        print("ID difficulty:", self.id)
##        print("Value minimus :", self.min)
##        print("Value maximus :", self.max)
##        print("Solver_output_type", self.solver_output_type)
##        print("Ouput folder", self.output_path)


    def verify_if_config_file_exist(self):
        """
        This method verify that config.xml exist in the folder /configurations
        Return True if the conf.xml file was found
        Return False if the conf.xml file was not found
        """
        try:
            file_path = self.get_configuration_path()
            fichero = open(file_path)
            fichero.close()
        except:
            return False
        return True

    def verify_xml_format(self):
        """
        This method verify that if the xml if the xml file is correct
        Return "False" if config.xml doesn't have the correct format
        Return "True" if config.xml have the correct format
        """
        if(self.verify_if_config_file_exist()):
            try:
                file_path = self.get_configuration_path()
                self.read_xml(file_path)
            except:
                print ("The config.xml doesnt have a format propely.Please verify the xml in the\
                       path:", self.path_of_file)
        else:
            return False


    def create_default_configuration_xml (self, file_path):
        """
        This method creates the xml file if this file not exists
        Return "True" if config.xml could be generate
        file_path > it has the file path in order to open it
        """
        try:
            xmlfile=open(file_path, "w")
            xmlfile.write("<?xml version='1.0' encoding='utf-8'?>\n")
            xmlfile.write("<configuration>\n")
            xmlfile.write("\t<default name=\"Default_conf\">\n")
            xmlfile.write("\t\t<algorithm>test1</algorithm>\n")
            xmlfile.write("\t\t<difficulty>test2</difficulty>\n")
            xmlfile.write("\t\t<solver_output_type>test3</solver_output_type>\n")
            xmlfile.write("\t\t<path_output>c:\\\\temp</path_output>\n")
            xmlfile.write("\t</default>\n")
            xmlfile.write("\t<levels>\n")
            xmlfile.write("\t\t<level id=\"0\" max=\"88\" min=\"20\" name=\"Easy\" />\n")
            xmlfile.write("\t\t<level id=\"1\" max=\"49\" min=\"46\" name=\"Medium\" />\n")
            xmlfile.write("\t\t<level id=\"2\" max=\"47\" min=\"65\" name=\"Hard\" />\n")
            xmlfile.write("\t</levels>\n")
            xmlfile.write("</configuration>\n")
            xmlfile.close()
        except:
            return ("default config.xml cannot be created in the path:", self.path_of_file)


    def create_folders_are_not_exist(self):
        """
        This method verify that the folders "configurations" and "output" are created
        If these folders are not created, this method creates these folders
          + This function is called be constructor in order to verify the folder structure
            of game
        """
        path_conf = self.path_of_file
        path_output = self.output_path
        try:
            if (not(os.path.exists (path_conf))):
                os.mkdir(path_conf)
            if (not(os.path.exists (path_output))):
                os.mkdir(path_output)
            return True
        except:
            return False

    def modify_value_in_xml(self, value,item):
        """
        This method modify the nodes "algorithm", 'difficulty', 'solver_output_type'
        , 'path_output' in the xml of configuration
        In the variable value has the type of 'algorithm', 'difficulty',
        'solver_output_type', 'path_output'
        The xml file will be modified
        """
        if(self.verify_if_config_file_exist()):
            file_path = self.get_configuration_path()
            tree = xmltree.parse(file_path)
            root = tree.getroot()
            self.algorithm = value
            for algorithm in root.iter(item):
                algorithm.text = str(value)
            tree.write(file_path, encoding ='utf-8', xml_declaration = True)

    def modify_levels(self, level, min_zeros, max_zeros):
        """
        level -> name of level, min_zeros-> minimums number of zeros ,max_zeros -> maximums
        number of zeros
        The xml file will be modified
        """
        if(self.verify_if_config_file_exist()):
            file_path = self.get_configuration_path()
            if(min_zeros<max_zeros):
                tree = xmltree.parse(file_path)
                root = tree.getroot()
                self.id = 0
                self.max = max_zeros
                self.min = min_zeros
                self.difficulty = level
                for levels in root.iter('level'):
                    leve_attrib = levels.attrib
                    if leve_attrib['name'] == level :
                        leve_attrib['min'] = str(min_zeros)
                        leve_attrib['max'] = str(max_zeros)
                        tree.write(file_path, encoding='utf-8', xml_declaration = True)

                return True
            else:
                return ("Value min must be less that max")

    def add_levels(self, level, min_zeros, max_zeros):
        """"
        level -> name of level, min_zeros-> minimums number of zeros ,max_zeros -> maximums
        number of zeros
        The xml file will be modified and the level should be added in the xml
        """
        file_path = self.get_configuration_path()
        if(self.verify_if_config_file_exist()):
            if(min_zeros<max_zeros):
                tree = xmltree.parse(file_path)
                root = tree.getroot()
                attributes = {"id":str(self.get_number_of_levels()),"max":str(max_zeros),
                              "min":str(min_zeros),"name":str(level)}
                for config in root.findall('levels'):
                    level_root = config
                    child = xmltree.SubElement(level_root,'level',attributes)
                tree.write(file_path,encoding ='utf-8', xml_declaration = True)
            else:
                return ("Value min must be less that max")

    def modify_path_conf_file(self, folder_path ,file_name = "config.xml"):
        """
        This method modify the path of config.xml file into the object
        """
        self.name_of_file = file_name
        self.path_of_file = folder_path

    def modify_path_output(self, output_folder):
        """
        This method will modify the output path in the object
        """
        self.output_path = output_folder


    def get_number_of_levels(self):
        """
        This is an internal method that get the number of levels creates in xml file
        Return the number of levels in the xml file
        """
        if(self.verify_if_config_file_exist()):
            file_path = self.get_configuration_path()
            tree = xmltree.parse(file_path)
            root = tree.getroot()
            cont = 0

            for levels in root.iter('level'):
                cont = cont + 1
            return cont

    def get_configuration_path(self):
        """
        This is an internal method that gets the path of configuration file and the name
        of configuration file
        Return the number of levels in the xml file
        """
        file_path = self.path_of_file + self.name_of_file
        return file_path

    def read_xml(self, file_name):
        """
        It receives an xml file and return root, it has the xml file data
        file_name > receives the xml path name
        """
        try:
            self.tree = xmltree.parse(file_name)
            return self.tree.getroot()
        except:
            self.tree = xmltree.parse(self.get_configuration_path())
            return self.tree.getroot()

    def get_value_from_xml(self, root, tag):
        """
        It receives root (it contains the xml file data)> returns the attribute name
        of the Configuration tag as string.
        root > it has the configuration xml file as a tree object
        """
        value = ""
        file_path = self.get_configuration_path()
        tree = xmltree.parse(file_path)
        root = tree.getroot()
        for node in root.findall('default'):
            value = node.find(tag).text
        return value

    def verify_modif_tag(self, tag, value):
        """
        This method verifies Tag modification, it returns True if the modification was successfully
        tag > this is a tag of the xml file, it can take the following values: algorithm,
              difficulty, solver_output_type and path_output
        value > this variable will change at value tag of the xml coniguration file
        """

        self.modify_value_in_xml(value,tag)
        root = self.read_xml(self.get_configuration_path())
        if (self.get_value_from_xml(root,'algorithm') == value):
           return True
        elif (self.get_value_from_xml(root,'difficulty') == value):
            return True
        elif (self.get_value_from_xml(root,'solver_output_type')  == value):
            return True
        elif (self.get_value_from_xml(root,'path_output') == value):
            return True
        else:
            return False

