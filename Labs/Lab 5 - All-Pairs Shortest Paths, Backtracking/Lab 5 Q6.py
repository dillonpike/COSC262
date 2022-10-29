import copy

def latin_squares(square):
    """Given a square (matrix) computes and returns Latin squares
    that can be obtained by replacing Nones with digits."""
    solutions = []
    dfs_backtrack(square, solutions)
    return solutions


def dfs_backtrack(candidate, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate):
            dfs_backtrack(child_candidate, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(copy.deepcopy(candidate))


def square_from_str(square_str):
    """Takes a string representation of a square and returns a matrix                                                                                                              
    (list of lists) representation where blanks are replaced with None."""
    return [[None if c == '-' else int(c) for c in line.strip()] for
            line in square_str.splitlines()]


def square_to_str(square):
    """Returns the string representation of the given square matrix."""
    return '\n'.join(''.join(str(c) for c in row) for row in square)


def is_solution(candidate):
    """Returns True if the candidate is a complete solution"""
    n = len(candidate)
    for i in range(n):
        if None in candidate[i]:
            return False
    return True


def children(candidate):
    """Returns a collestion of candidates that are the children of the given
    candidate."""
    candidates = []
    n = len(candidate)
    for i in range(n):
        for j in range(n):
            if candidate[i][j] == None:
                row = i
                column = j
                
    inputs = {num for num in range(n)} - set(candidate[row])
    for i in range(n):
        inputs -= {candidate[i][column]}
    for num in inputs:
        candidate_copy = copy.deepcopy(candidate)
        candidate_copy[row][column] = num
        candidates.append(candidate_copy)    
    
    return candidates

    
def should_prune(candiate):
    """Returns True if the tree should be pruned at this point."""
    return False
    

square = [
    [0,    1],
    [None, 0],
]


solutions = latin_squares(square)
print("Number of solutions:", len(solutions))
for solution in solutions:
    print(square_to_str(solution))

square_str = """\
01
-1
"""

square = square_from_str(square_str)
print(latin_squares(square))

square = [[None]]
print(latin_squares(square))

square_str = """\
0123
-0--  
--0- 
----    
"""

square = square_from_str(square_str)
for solution in sorted(latin_squares(square)):
    print(square_to_str(solution), end="\n\n")
