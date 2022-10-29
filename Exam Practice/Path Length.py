def path_length(parent, start, end):
    counter = 0
    while end is not None and end != start:
        end = parent[end]
        counter += 1
    if end is None:
        counter = float('inf')
    return counter

print(path_length([None, 0], 0, 1))
print(path_length([None, None], 0, 0))
print(path_length([None, None], 0, 1))
print(path_length([None, 2, 3, None, 3, 4], 3, 5))