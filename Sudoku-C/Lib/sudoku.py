from copy import copy
import math
import random
import time

MIN = -1
EASY = 0
MEDIUM = 1
HARD = 2
EXPERT = 3
INSANE = 4
GOOD_LUCK = 5

class Sudoku(object):
    SCALE =  {MIN: 0.50,EASY: 0.40,MEDIUM: 0.35,HARD: 0.30,EXPERT: 0.24, INSANE: 0.17, \
              GOOD_LUCK: 0.12,}
    def __init__(self, grid_size=3, difficulty=MEDIUM):
        """
        It is the constructor of the object
        """
        self.set_grid_size(grid_size)
        self.set_difficulty(difficulty)
        self.side_length = self.grid_size ** 2
        self.square = self.side_length ** 2
        self.possibles = set([i + 1 for i in range(self.side_length)])
        self.solution = []
        self._masked = None
        self.iterations = 0
        self.clear()

    def reset(self,difficulty=0):
        """
        Initializa the object in order to generate other
        """
        self.set_difficulty(difficulty)
        self.possibles = set([i + 1 for i in range(self.side_length)])
        self.solution = []
        self._masked = None
        self.iterations = 0
        self.clear()

    def set_grid_size(self, grid_size):
        """
        Set configure the grid size into the object
        """
        self.grid_size = grid_size

    def set_difficulty(self, difficulty):
        """
        Set the difficulty into the object
        """
        self.difficulty = difficulty

    def get_row(self, row):
        """Returns all values for the specified row"""
        start = row * self.side_length
        end = start + self.side_length
        return self.solution[start:end]

    def set_row(self, row, values):
        """Sets the values for the specified row"""

        start = row * self.side_length
        end = start + self.side_length
        self.solution[start:end] = values

    def get_col(self, col):
        """Returns all values for the specified column"""

        return self.solution[col::self.side_length]

    def set_col(self, col, values):
        """Sets the values for the specified column"""

        self.solution[col::self.side_length] = values

    def get_region(self, row, col):
        """Returns all values for the region at the given (row, col)"""
        start_row = int(row / self.grid_size) * self.grid_size
        start_col = int(col / self.grid_size) * self.grid_size
        values = []
        for i in range(self.grid_size):
            start = (start_row + i) * self.side_length + start_col
            end = start + self.grid_size
            values.extend(self.solution[start:end])
        return values

    def clear(self):
        """Cleans up the Sudoku solution"""
        self.solution = [None for i in range(self.square)]

    def __index_to_row_col(self, index):
        """Translates an index in our 1-dimensional list to a (row, col)"""
        return divmod(index, self.side_length)

    def get_used(self, row, col):
        """Returns a list of all used values for a row, column, and region"""
        r = self.get_row(row)
        c = self.get_col(col)
        region = self.get_region(row, col)
        return (r + c + region)

    def get_used_by_index(self, index):
        """Returns a list of all used values for a row, col, and region"""
        row, col = self.__index_to_row_col(index)
        return self.get_used(row, col)

    def is_valid_value(self, row, col, value):
        """
        Validates whether or not a value will work in the grid, without using
        the pre-generated solution
        """
        return value not in self.get_used(row, col)

    def fill_square(self, index=0):
        """
        Recursively populates each square on the Sudoku grid until a solution
        is found.  Most of this method was inspired by Jeremy Brown
        """
        if self.solution[index]:
            if index + 1 >= self.square:
                return True
            return self.fill_square(index + 1)
        used = self.get_used_by_index(index)
        possible = list(self.possibles.difference(used))
        if len(possible) == 0:
            return False
        random.shuffle(possible)
        for new_value in possible:
            self.solution[index] = new_value
            self.iterations += 1
            if index + 1 >= self.square or self.fill_square(index + 1):
                return True
            self.solution[index] = None
        return False

    def generate(self):
        """
        Fill a sudoku
        """
        self.iterations = 0
        self.fill_square(0)

    @property
    def masked_grid(self):
        """Generates and caches a Sudoku with several squares hidden"""
        if self._masked is None:
            self._masked = copy(self.solution)
            min = math.ceil(Sudoku.SCALE[self.difficulty] * self.square)
            max = math.ceil(Sudoku.SCALE.get(self.difficulty - 1, min) * self.square)
            numbers_to_show = random.randint(min, max)

            uncleared_squares = [i for i in range(len(self.solution))]
            for i in range(self.square - numbers_to_show):
                index = random.choice(uncleared_squares)
                self._masked[index] = '0'
                uncleared_squares.remove(index)
        return self._masked

    def get_puzzle_array(self):
        """
        return the Sudoku generated with zeros in an array
        """
        return self.masked_grid

    def get_solution_array(self):
        """
        return the solution of Sudoku in an array
        """
        return self.solution

    def get_puzzle_srt(self):
        """
        return the Sudoku generated with zeros in an array
        """
        board = ""
        size = len(self.masked_grid)
        for i in range (size):
            board += str(self.masked_grid[i])
        return board

    def get_solution_str(self):
        """
        return the solution of Sudoku in an array
        """
        board = ""
        size = len(self.solution)
        for i in range (size):
            board += str(self.solution[i])
        return board

    def get_number_of_zeros(self):
        """
        Get the number of zeros in the sudoku
        """
        size = len(self.masked_grid)
        counter = 0
        for i in range (size):
            if (self.masked_grid[i] == '0'):
                counter +=1
        return counter

    def generated_next_sudoku(self,difficulty):
        """
        Get a new Sudoku if a solution doesnt exist
        """
        self.reset(difficulty)
        self.generate()
        zeros =self.get_number_of_zeros()
        return zeros

    def get_sudoku(self,min_segment,max_segment):
        """
        Calculates a new Sudoku
        """
        numbers_zeros = random.randint(min_segment,max_segment)
        if (numbers_zeros >= 41 and numbers_zeros <= 72):
            inserted_zeros = 0
            counter = 0
            while (inserted_zeros!= numbers_zeros):
                if (numbers_zeros >= 41 and numbers_zeros <= 48):
                        level = 0
                        inserted_zeros = self.generated_next_sudoku(level)
                if(numbers_zeros > 48 and numbers_zeros < 61):
                        level = random.randint(1,3)
                        inserted_zeros = self.generated_next_sudoku(level)
                if(numbers_zeros >= 61 and numbers_zeros <= 67):
                        level = random.randint(2,4)
                        inserted_zeros = self.generated_next_sudoku(level)
                if(numbers_zeros > 67 and numbers_zeros <= 72):
                        level = 5
                        inserted_zeros = self.generated_next_sudoku(level)
                counter +=1
                if (counter >= 100):
                    self.generated_next_sudoku(level)
                    numbers_zeros = random.randint(min_segment,max_segment)
            return self.get_puzzle_srt()
        else:
            return "None"
