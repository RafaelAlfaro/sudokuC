import sys
sys.path.append("../lib")
from coverage import coverage
cov = coverage()
cov.start()

import unittest
from test_recursive_solver import Testrecursive
from test_string import TestString
from test_peter_algorithm import TestPeterAlgorithm
from test_backtraking import UnitTestBacktrak
from test_configuration import TestConfiguration
from test_cvs_format import Test_cvs_format
from test_file_txt import TestFileTxt
from test_htmlsudoku import Test_Htmlsudoku
from test_sudoku_gen import Test_sudoku_gen

suite = unittest.TestSuite()

suite.addTests(unittest.makeSuite(TestConfiguration))
suite.addTests(unittest.makeSuite(Testrecursive))
suite.addTests(unittest.makeSuite(TestString))
suite.addTests(unittest.makeSuite(TestPeterAlgorithm))
suite.addTests(unittest.makeSuite(UnitTestBacktrak))
suite.addTests(unittest.makeSuite(Test_cvs_format))
suite.addTests(unittest.makeSuite(TestFileTxt))
suite.addTests(unittest.makeSuite(Test_Htmlsudoku))
suite.addTests(unittest.makeSuite(Test_sudoku_gen))

unittest.TextTestRunner(verbosity=2).run(suite)
cov.stop()
cov.html_report(directory='coverage_report')