import time
class peter_algorithm:
    """
	Function that elaborates a square by 9 x 9 , where the
        receive_values_of_rows receives string like: 'ABCDEFGHI' and
        receive_values_of_digits receives string like: '123456789'
	"""
    def cross(self, receive_values_of_rows, receive_values_of_digits):
        return [one_row + one_digit for one_row in receive_values_of_rows \
                for one_digit in receive_values_of_digits]

    def __init__(self):
        """
		Constructor that defines parameters to develop the game.
		"""
        self.time_solve = 0.0
        self.digits   = '123456789'
        self.rows     = 'ABCDEFGHI'
        self.cols     = self.digits
        self.squares  = self.cross(self.rows,self.cols)
        self.unitlist = ([self.cross(self.rows, column) for column in self.cols] +
                         [self.cross(row, self.cols) for row in self.rows] +
                         [self.cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in \
                         ('123','456','789')])
        self.units    = dict((square_value, [unit for unit in self.unitlist \
                        if square_value in unit]) for square_value in self.squares)
        self.peers    = dict((square_value, set(sum(self.units[square_value],[])) - set([square_value])) \
                        for square_value in self.squares)

    def parse_grid_in_dictionary(self, grid):
        """
		Convert grid to a dict of possible values, {square: digits}, or
            return False if a contradiction is detected.
		"""
        values = dict((square_value, self.digits) for square_value in self.squares)
        for square_value, digit in self.grid_values(grid).items():
            if digit in self.digits and not self.assign(values, square_value, digit):
                return(False)
        return(values)

    def grid_values(self, grid):
        """
		Convert grid into a dict of {square: char} with '0' or '.'
        for empties.
		"""
        chars = [column for column in grid if column in self.digits or column in '0.']
        if len(chars) == 81:
            return(dict(zip(self.squares, chars)))

    def assign(self, values, square_value, digit):
        """
		Eliminate all the other values (except digit) from values
        [square_value] and propagate. Return values, except return
        False if a contradiction is detected.
		"""
        other_values = values[square_value].replace(digit, '')
        if all(self.eliminate(values, square_value, auxiliary_digit) \
               for auxiliary_digit in other_values):
            return(values)
        else:
		return(False)

    def eliminate(self, values, square_value, digit):
        """
		Eliminate digit from values[square_value]; propagate when values
        or places <= 2. Return values, except return False if a contradiction
        is detected.
		"""
        if digit not in values[square_value]:
            return(values)
        values[square_value] = values[square_value].replace(digit, '')
        if len(values[square_value]) == 0:
            return(False)
        elif len(values[square_value]) == 1:
            auxiliary_digit = values[square_value]
            if not all(self.eliminate(values, square_auxiliary, auxiliary_digit) \
               for square_auxiliary in self.peers[square_value]):
                return(False)
        for unit in self.units[square_value]:
            row_complete_in_dictionary = [square_value for square_value in unit if digit\
                                         in values[square_value]]
            if len(row_complete_in_dictionary) == 0:
                return(False)
            elif len(row_complete_in_dictionary) == 1:
                if not self.assign(values, row_complete_in_dictionary[0], digit):
                    return(False)
        return values

    def display(self, values):
        """
		Displays a square of 9 x 9 and the values the sudoku.
        These values can be an unsolved game or a game resolved.
		"""
        width = 1 + max(len(values[square_value]) for square_value in self.squares)
        line = '+'.join(['-' * (width * 3)] * 3)
        for row in self.rows:
            print ''.join(values[row + column].center(width)+('|' if column in '36' else '')
                          for column in self.cols)
            if row in 'CF': print line

    def solve(self, grid):
        """
		Receive the game_solution function a grid, el grid the grid is
        transformed to dictionaries using the parse_grid_in_dictionary function
        and start searching the solution using depth-first search and
        propagation, try all possible values.
        When the solution is found the search function returns the variable
        values.This has the solution
		"""
        return self.search(self.parse_grid_in_dictionary(grid))

    def search(self, values):
        """
		Using depth-first search and propagation, try all possible values.
		"""
        if values is False:
            return(False)
        if all(len(values[square_value]) == 1 for square_value in self.squares):
            return(values)
        n,square_value = min((len(values[square_value]), square_value) \
        for square_value in self.squares if len(values[square_value]) > 1)
        return self.some(self.search(self.assign(values.copy(), square_value, digit))
                    for digit in values[square_value])

    def some(self, seq):
        """
		Return some element of seq when  is true.
        The seq variable receives values from assing and search functions
		"""
        for e in seq:
            if e: return(e)
        return False

    def parse_grid_and_grouped_into_nine_digits(self, value_grid):
        """
		Parse a grid and adds the separator of nine characters.
		"""
        size = len (value_grid)
        group_nine_digits = 9
        str_final =""
        for explore_grid in range(size):
            if explore_grid == group_nine_digits:
                str_final += '\n'
                group_nine_digits += 9
            str_final += value_grid[explore_grid]
        str_final += '\n'
        return(str_final)

    def game_solution (self,grid):
        """
		Receive an game without resolve (variable grid), the grid is
        transformed to dictionaries and start a search  using depth-first
        search and propagation, try all possible values.
        Return the game solved in the puzzle_solved variable.
		"""
        puzzle_solved = ""
        start = time.clock()
        values = self.solve(grid)
        time_of_resolution = time.clock()-start
        self.time_solve = time_of_resolution
        puzzle_sort = sorted(dict.items(values))
        for individual_square_position in range (0,81):
            value_individual_per_square = puzzle_sort[individual_square_position][1]
            puzzle_solved += str(value_individual_per_square)
        return(str(puzzle_solved))

    def get_time(self):
        """
		Function that returns the time that a game has been solved by the algorithm.
		"""
        return(self.time_solve)

