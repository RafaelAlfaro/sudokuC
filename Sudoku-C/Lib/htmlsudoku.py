import time
class Htmlsudoku:
      def __init__(self):
          """
            This method is the constructor  of the object. it  will initialize the variables
            used in the object:
            Variables with templates to build the html. the words with "@" will be remplaced in the
            methods.
             self.header_start
             self.table_begin
             self.thead_start
             self.th_column
             self.thead_end
             self.tbody_start
             self.tr_start
             self.th_row
             self.td_board
             self.tr_end
             self.tbody_end
             self.table_end
             self.body_end
             self.header_end

          rows - List of row names in the puzzle
          board_colors - [0] : border color
                         [1..9] : block of color
                        -------------
                        | 1 | 2 | 3 |
                         --+---+---
                        | 4 | 5 | 6 |
                         --+---+---
                        | 7 | 8 | 9 |
                        -------------

          """
          self.header_start = "<html>\n<head>\n<title>@title</title>\n</head>\n"
          self.body_start = "<body>\n"
          self.table_begin_aux ="<table summary=\"@caption\" border=@value align=\"center\">"
          self.table_begin = self.table_begin_aux +"\n<caption>@caption</caption>\n"
          self.thead_start = "<thead>\n<tr>\n"
          self.th_column = "<th scope=\"col\" bgcolor=#@color width= 10 align= \"center\">@value</th>\n"
          self.thead_end = "</tr>\n</thead>\n"
          self.tbody_start = "<tbody>\n"
          self.tr_start = "<tr>\n"
          self.th_row = "<th scope=\"row\" bgcolor=#@color width= 20 align= \"center\">@value</th>\n"
          self.td_board = "<td bgcolor=#@color align= \"center\">@value</td>\n"
          self.tr_end = "</tr>\n"
          self.tbody_end = "</tbody>\n"
          self.table_end = "</table>\n"
          self.body_end = "</body>\n"
          self.header_end = "</html>\n"
          self.rows = "_ABCDEFGHI"
          self.board_colors = ["FFFFFF","FF8AD8","F592FF","E6FF92","95FF92","BFCDD5","92FFCE",\
                               "92D2FF","92A0FF","BC92FF"]

      def get_board_color(self, block):
          """
          Return the color assigned to the block.
          Keyword arguments:
          block - the numbero of block [1..9]
          """
          block += 1
          block_1 = [1,2,3,10,11,12,19,20,21]
          block_2 = [4,5,6,13,14,15,22,23,24]
          block_3 = [7,8,9,16,17,18,25,26,27]
          block_4 = [28,29,30,37,38,39,46,47,48]
          block_5 = [31,32,33,40,41,42,49,50,51]
          block_6 = [34,35,36,43,44,45,52,53,54]
          block_7 = [55,56,57,64,65,66,73,74,75]
          block_8 = [58,59,60,67,68,69,76,77,78]
          block_9 = [61,62,63,70,71,72,79,80,81]
          if block in block_1:
            return (self.board_colors[1])
          if block in block_2:
            return (self.board_colors[2])
          if block in block_3:
            return (self.board_colors[3])
          if block in block_4:
            return (self.board_colors[4])
          if block in block_5:
            return (self.board_colors[5])
          if block in block_6:
            return (self.board_colors[6])
          if block in block_7:
            return (self.board_colors[7])
          if block in block_8:
            return (self.board_colors[8])
          if block in block_9:
            return (self.board_colors[9])


      def mofify_header(self, title):
          """
          This method customizes the header of html.
          Keyword arguments:
            title : the value of this variable is replaced in the string header_start
          return : the string modified
          """
          html_generated = self.header_start.replace("@title", title)
          return(html_generated)

      def modify_table_header(self, caption, borde=1):
          """
          This method customizes the header of the table in html.
          Keyword arguments:
            caption : The value of this variable is replaced in the string table_begin
            borde : the border used in the table can be modified. The value by default is "1"
          return : the string modified

          """
          html_generated = self.table_begin.replace("@caption", caption)
          html_generated = html_generated.replace("@value", str(borde))
          return(html_generated)

      def modify_th_column(self, color, value):
          """
          This method customizes the column of table in the html
          Keyword arguments:
            color : The value of this variable is replaced in the string th_column
            value : The value is replaced in the string th_column. This is the name of column
          return : the string modified
          """
          html_generated = self.th_column.replace("@color", color)
          html_generated = html_generated.replace("@value", value)
          return(html_generated)

      def make_columns(self):
          """
          Return the columns modified
          """
          html_generated = ""
          for column in self.rows:
              html_generated += self.modify_th_column(self.board_colors[0], column)
          return(html_generated)

      def generate_table(self, puzzle):
          """
          This method generates the table in HTML format.
          Keyword arguments:
            puzzle : the sudoku in a string
          return : a tring with the table formated

          """
          size = len(puzzle)
          html_generated = ""
          row = 1
          rows_start = [0,9,18,27,36,45,54,63,72]
          rows_end = [8,17,26,35,44,53,62,71,80]
          for cell in range(size):
              if (cell in rows_start):
                 auxiliar_html = self.tr_start
                 auxiliar_html = self.th_column.replace("@color", self.board_colors[0])
                 auxiliar_html = auxiliar_html.replace("@value", self.rows[row])
                 html_generated += auxiliar_html
                 row += 1
              auxiliar_html = self.td_board.replace("@color", self.get_board_color(cell))
              auxiliar_html = auxiliar_html.replace("@value", puzzle[cell])
              html_generated += auxiliar_html
              if(cell in rows_end):
                      html_generated += self.tr_end

          return(html_generated)


      def make_table(self,puzzle, title):
          """
          This method generates the table with the data in the puzzle
          Keyword arguments:
            puzzle : The sudoku in line format
            title : The title of puzzle
          return : return the table generated in a string
          """

          html_generated = ""
          html_generated += self.modify_table_header(title)
          html_generated += self.thead_start
          html_generated += self.make_columns()
          html_generated += self.thead_end
          html_generated += self.tbody_start
          html_generated += self.generate_table(puzzle)
          html_generated += self.table_end
          html_generated += self.tbody_end
          return(html_generated)


      def get_html(self,puzzle,result=""):
          """
          This method builds the html
          Keyword arguments:
            puzzle : The sudoku in line format
            return : This parameter will be use to generate a html with sudoku and the solution in
                     a html
          return : return the html generated in a string
          """
          html_generated = ""
          html_generated += self.mofify_header("Sudoku board")
          html_generated += self.body_start
          html_generated += self.make_table(puzzle,"Sudoku")
          if(result != ""):
              html_generated += self.make_table(result,"Result")
          html_generated += self.body_end
          html_generated += self.header_end
          return(html_generated)

      def generate_name(self, file_name=""):
          """
          This method generates names for the files with the time in the system
           Keyword arguments:
            file_name : With this name is empty this is generated with: "sudoku_[HMSMDY]"
                        The name of file can be configurable : "puzzle_[HMSMDY]"
                        [%H%M%S%m%d%Y] == [Hour ,Minutes ,seconds ,Mount ,Day ,Year]
          return : return a name to use in the name file
          """
          get_time = time.strftime('%H%M%S%m%d%Y')

          if (file_name == ""):
             file_name = "sudoku_" + get_time + ".html"
          else:
             file_name += "_"
             file_name = file_name + get_time + ".html"
          return(file_name)

      def html_to_file(self, html_result, file_path, name = ""):
          """
          This method creates the html in the path specified.
          Keyword arguments:
            html_result : the html in a string
            file_path : the path of output
            name : The name of file

          """
          try:
              file_name = self.generate_name(name)
              file_path += "\\" + file_name
              f = open(file_path ,"w")
              f.write(html_result)
              f.close
          except:
                 return("The file cannot be written")
