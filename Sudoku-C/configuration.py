#-------------------------------------------------------------------------------
# Name:        configuration
# Purpose: The purpose of this test case is handle a XML. This xml will be said config.xml
#          The config.xml contains the configration of Sudoku game:
#          algorithm : This atribute will contain the algorithm to be use by default.
#				Peter_n
#				Backtraking
#				Other : TBD
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
        self.path_of_file = os.getcwd() + "\\configurations\\"
        self.algorithm = "Backtraking"
        self.difficulty = "Easy"
        self.id = "1"
        self.min = "46"
        self.max = "49"
        self.solver_output_type = "txt"
        self.output_path = os.getcwd() + "\\outputs\\"
        self.name = "configuration"

    def print_configuration (self):
        """
        This method prints the variables of object
        algorithm - Algorithm used
        difficulty - Difficulty used
        id - id of level
        min - minimums hold in the board
        max - Maximus hold in the board
        solver_output_type - type of output (txt or cvs)
        output_path - the path of output

        """
        print("Name : ", self.name_of_file)
        print("Path of scrypt :", self.path_of_file)
        print("Algorithm:", self.algorithm)
        print("Difficulty:", self.difficulty)
        print("ID difficulty:", self.id)
        print("Value minimus :", self.min)
        print("Value maximus :", self.max)
        print("Solver_output_type", self.solver_output_type)
        print("Ouput folder", self.output_path)


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
            print ("config.xml must be in the path :", self.path_of_file)
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
            print ("default config.xml cannot be created in the path:", self.path_of_file)


    def create_folders_are_not_exist(self):
        """
        This method verify that the folders "configurations" and "output" are created
        If these folders are not created, this method creates these folders
          + This function is called be constructor in order to verify the folder structure
            of game
        """
        path_conf = self.path_of_file
        path_output = self.output_path
        if (not(os.path.exists (path_conf))):
            os.mkdir(path_conf)
        if (not(os.path.exists (path_output))):
            os.mkdir(path_output)

    def modify_algorithm(self, type_algorithm):
        """
        This method modify the node "algorithm" in the xml of configuration
        In the variable "type_algorithm" has the type of algorithm
        The xml file will be modified
        """
        if(self.verify_if_config_file_exist()):
            file_path = self.get_configuration_path()
            tree = xmltree.parse(file_path)
            root = tree.getroot()
            self.algorithm = type_algorithm
            for algorithm in root.iter('algorithm'):
                algorithm.text = str(type_algorithm)
            tree.write(file_path, encoding ='utf-8', xml_declaration = True)

    def modify_difficulty(self, level_difficulty):
        """
        This method modify the node "difficulty" in the xml of configuration
        In the variable "level_difficulty" has the level of difficulty
        The xml file will be modified
        """
        if(self.verify_if_config_file_exist()):
            file_path = self.get_configuration_path()
            tree = xmltree.parse(file_path)
            root = tree.getroot()
            self.difficulty = level_difficulty
            for difficulty in root.iter('difficulty'):
                difficulty.text = str(level_difficulty)
            tree.write(file_path,encoding='utf-8', xml_declaration=True)

    def modify_solver_output_type(self, type_ouput):
        """
        This method modify the node "level_type_ouput" in the xml of configuration
        In the variable "type_ouput" has the type of output
        The xml file will be modified
        """
        if(self.verify_if_config_file_exist()):
            file_path = self.get_configuration_path()
            tree = xmltree.parse(file_path)
            root = tree.getroot()
            self.solver_output_type = type_ouput
            for solver_output_type in root.iter('solver_output_type'):
                solver_output_type.text = str(type_ouput)
            tree.write(file_path, encoding = 'utf-8', xml_declaration = True)

    def modify_path_output(self, output):
        """
        This method modify the node "path_output" in the xml of configuration
        In the variable "output" has the path of outputs
        The xml file will be modified
        """
        if(self.verify_if_config_file_exist()):
            file_path = self.get_configuration_path()
            tree = xmltree.parse(file_path )
            root = tree.getroot()
            self.output_path = output
            for path_output in root.iter('path_output'):
                path_output.text = str(output)
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
            else:
                print ("Value min must be less that max")

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
                print ("Value min must be less that max")

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

    def get_name(self, root):
        """
        It receives root (it contains the xml file data)> returns the attribute name
        of the Configuration tag as string.
        root > it has the configuration xml file as a tree object
        """
        for config in root.findall('default'):
            name = config.get('name')
            if name != "":
                self.name = name
                return name
            else:
                return self.name

    def get_algorithm(self, root):
        """
        It receives root (it contains the xml file data)> returns the ALGORITHM
        tag value as string.
        if this value is empty, it returns the ALGORITHM default value as string.
        root > it has the configuration xml file as a tree object
        """
        for config in root.findall('default'):
            algorithm = config.find('algorithm').text
            if algorithm != " ":
                return algorithm
            else:
                return self.algorithm

    def get_difficulty(self, root):
        """
        It receives root (it contains the xml file data)> returns the Difficulty
        tag value as string.
        if this value is empty, it returns the Difficulty default value as string.
        root > it has the configuration xml file as a tree object
        """
        for config in root.findall('default'):
            difficulty = config.find('difficulty').text
            if difficulty != " ":
                return difficulty
            else:
                return self.difficulty

    def get_solver_output_type(self, root):
        """
        It receives root (it contains the xml file data)> returns the "solver_output_type"
        tag value as string.
        if this value is empty, it returns the "solver_output_type" default value as string.
        root > it has the configuration xml file as a tree object
        """
        for config in root.findall('default'):
            solver_output_type = config.find('solver_output_type').text
            if solver_output_type != " ":
                return solver_output_type
            else:
                return self.solver_output_type

    def get_path_output(self, root):
        """
        It receives root (it contains the xml file data)> returns the "path_output" tag value
        as string.
        if this value is empty, it returns the "path_output" default value as string.
        root > it has the configuration xml file as a tree object
        """
        for config in root.findall('default'):
            path_output = config.find('path_output').text
            if path_output != " ":
                return path_output
            else:
                return self.output_path

    def verify_modif_tag(self, tag, value):
        """
        This method verifies Tag modification, it returns True if the modification was successfully
        tag > this is a tag of the xml file, it can take the following values: algorithm,
              difficulty, solver_output_type and path_output
        value > this variable will change at value tag of the xml coniguration file
        """
        if tag == "algorithm":
            self.modify_algorithm(value)
            root = self.read_xml(self.get_configuration_path())
            if self.get_algorithm(root) == value:
                return True
            else:
                return False
        elif tag == "difficulty":
            self.modify_difficulty(value)
            root = self.read_xml(self.get_configuration_path())
            if self.get_difficulty(root) == value:
                return True
            else:
                return False
        elif tag == "solver_output_type":
            self.modify_solver_output_type(value)
            root = self.read_xml(self.get_configuration_path())
            if self.get_solver_output_type(root) == value:
                return True
            else:
                return False
        elif tag == "path_output":
            self.modify_path_output(value)
            root = self.read_xml(self.get_configuration_path())
            if self.get_path_output(root) == value:
                return True
            else:
                return False
