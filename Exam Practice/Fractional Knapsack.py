def fractional_knapsack(capacity, items):
    items_copy = items[:]
    items_copy.sort(key=lambda x: x[1] / x[2], reverse=True)
    max_value = 0
    for name, value, weight in items_copy:
        if weight < capacity:
            max_value += value
            capacity -= weight
        else:
            max_value += value * capacity / weight
            break
    return max_value

# The example from the lecture notes
items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(fractional_knapsack(9, items))