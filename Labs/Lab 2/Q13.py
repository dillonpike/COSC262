def combinations(items, r):
    if r == 0:
        return [()]
    if r > len(items):
        return []
    combos = []
    combinations_helper(items, r, combos, [])
    return combos

def combinations_helper(items, r, combos, current):
    if len(current) == r:
        combos.append(tuple(current))
    else:
        for item in items:
            if len(current) == 0:
                combinations_helper(items, r, combos, current+[item])
            elif item > current[-1]:
                combinations_helper(items, r, combos, current+[item])


def combinations(items, r):
    if r == 0:
        return [()]
    if r > len(items):
        return []
    
    combos = []
    current = tuple()
    previous = tuple()
    
    combinations_helper(items, r, combos, current, previous)
    return combos

def combinations_helper(items, r, combos, current, previous):
    if len(current) == r:
        combos.append(current)   
    else:
        combinations_helper(items, r, combos, current, previous)

# Test is a bit complicated because of the need
# to handle any ordering of the list and the tuples.
ans = []
for combo in combinations([1, 2, 3, 4, 5, 6], 3):
    ans.append(tuple(sorted(combo)))
print(sorted(ans))

combos = []
for i in range(0, 10):
    combos += combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], i)
print(len(combos))