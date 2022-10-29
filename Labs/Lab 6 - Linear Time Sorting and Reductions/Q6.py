def key_positions(seq, key):
    k = max(key(x) for x in seq) + 1
    positions = [0 for i in range(k)]
    for element in seq:
        positions[key(element)] += 1
    total = 0
    for i in range(k):
        positions[i], total = total, total + positions[i]
    return positions

if __name__ == '__main__':
    print(key_positions([0, 1, 2], lambda x: x))
    print(key_positions([2, 1, 0], lambda x: x))
    print(key_positions([1, 2, 3, 2], lambda x: x))
    print(key_positions([5], lambda x: x))
    print(key_positions(range(-3,3), lambda x: x**2))
    print(key_positions(range(1000), lambda x: 4))
    print(key_positions([1] + [0] * 100, lambda x: x))
    print(key_positions([2, -2, 1], lambda x : x**2))