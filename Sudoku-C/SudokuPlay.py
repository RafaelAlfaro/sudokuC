#-------------------------------------------------------------------------------
# Name:    Sudoku play
# Purpose: This script run the sudoku game
# Author(s):
#           Carla Munoz <CM>
#           Gustavo Ramirez <GR>
#           Rafael Alfaro <RAM>
#
# Created:     07/23/2013
#-------------------------------------------------------------------------------
import sys
sys.path.append("lib")
import console_presentation

puzzle = "000000000000000000000000000000000000000000000000000000000000000000000000000000000"
sudoku_console = console_presentation.ConsolePresentation(puzzle)
sudoku_console.run_app(puzzle)

