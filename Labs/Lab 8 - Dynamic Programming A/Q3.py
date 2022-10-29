"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
import time
INFINITY = float('inf')  # Same as math.inf

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    known = {}
    def cell_cost(row, col):
        """The cost of getting to a given cell in the current grid."""
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return INFINITY  # Off-grid cells are treated as infinities
        else:
            cost = grid[row][col]
            if row != 0:
                choices = []
                for delta_col in range(-1, 2):
                    if (row - 1, col + delta_col) not in known:
                        cell = cell_cost(row - 1, col + delta_col)
                        choices.append(cell)
                        known[(row - 1, col + delta_col)] = cell
                    else:
                        choices.append(known[(row - 1, col + delta_col)])
                cost += min(choices)
            return cost
            
    best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
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