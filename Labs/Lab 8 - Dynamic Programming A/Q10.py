import sys
from functools import cache
import time
sys.setrecursionlimit(2000)

class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"


def max_value(items, capacity):
    
    @cache
    def inner_max(n, capacity):
        if n <= 0 or capacity <= 0:
            return 0
        elif items[n-1].weight > capacity:
            return inner_max(n-1, capacity)
        else:
            return max(items[n-1].value + inner_max(n-1, capacity - items[n-1].weight),
                       inner_max(n-1, capacity))
    
    return inner_max(len(items), capacity)

# The example from the lecture notes
items = [
    Item(45, 3),
    Item(45, 3),
    Item(80, 4),
    Item(80, 5),
    Item(100, 8)]
start = time.time()
print(max_value(items, 10))
end = time.time()
print("Time taken:", end - start)

items = [Item(i, 10) for i in range(1, 11)]
items.extend([Item(1, 5), Item(1, 4)])

print(max_value(items, 99))