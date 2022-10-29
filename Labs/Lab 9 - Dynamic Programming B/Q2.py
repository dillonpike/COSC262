import numpy as np

class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __repr__(self):
        return f"Item({self.value}, {self.weight})"
        
        
def max_value(items, capacity):
    """The maximum value achievable with a given list of items and a given
       knapsack capacity."""
    table = np.array([(capacity+1) * [0] for i in range(len(items)+1)])
    for i in range(1, len(items)+1):
        for c in range(1, capacity+1):
            if items[i-1].weight > c:
                table[i][c] = table[i-1][c]
            else:
                table[i][c] = max(table[i-1][c], items[i-1].value + table[i-1][c-items[i-1].weight])
    used = []
    i, c = len(items), capacity
    while i > 0 and c > 0:
        if table[i][c] != table[i-1][c]:
            used.append(items[i-1])
            c = c - items[i-1].weight
        i -= 1
    return (table[len(items)][capacity], used)

# The example in the lecture notes
items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
print(max_value(items, 10))