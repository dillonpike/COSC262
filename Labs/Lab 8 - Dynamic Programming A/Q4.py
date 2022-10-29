"""A program to read a grid of weights from a file and compute the 
   minimum cost of a path from the top row to the bottom row
   with the constraint that each step in the path must be directly
   or diagonally downwards. 
   This question has a large(ish) 200 x 200 grid and you are required
   to use a bottom-up DP approach to solve it.
"""
import numpy as np
import time
INFINITY = float('inf')

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = np.array([[int(bit) for bit in line.split()] for line in lines])
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given grid of
       integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    # **** Your code goes here. It must compute a value 'best', which is
    # the minimum cost from the top of the grid to the bottom.
    known = {}
    
    def cell_cost(row, col):
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return INFINITY  # Off-grid cells are treated as infinities
        else:
            cost = grid[row, col]
            if row != n_rows - 1:
                choices = []
                for delta_col in range(-1, 2):
                    choice = (row + 1, col + delta_col)
                    if choice not in known:
                        cell = cell_cost(choice[0], choice[1])
                        choices.append(cell)
                        known[choice] = cell
                    else:
                        choices.append(known[choice])
                cost += min(choices)
            return cost
        
    best = min(cell_cost(0, col) for col in range(n_cols))
    return best
    
    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))


print(file_cost('checkerboard.trivial.in'))
print(file_cost('checkerboard.small.in'))
start = time.time()
print(file_cost('checkerboard.medium.in'))
end = time.time()
print("Time taken:", end - start)