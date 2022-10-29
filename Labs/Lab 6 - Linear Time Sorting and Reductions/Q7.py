from Q6 import key_positions

def sorted_array(seq, key, positions):
    sorted_list = [0 for i in range(len(seq))]
    for element in seq:
        sorted_list[positions[key(element)]] = element
        positions[key(element)] += 1
    return sorted_list

if __name__ == '__main__':
    print(sorted_array([3, 1, 2], lambda x: x, [0, 0, 1, 2]))
    print(sorted_array([3, 2, 2, 1, 2], lambda x: x, [0, 0, 1, 4]))
    print(sorted_array([100], lambda x: x, [0]*101))
    print(sorted_array([2, -2, 1], lambda x: x**2, [0, 0, 1, 1, 1]))
    """Counting Sort"""
    import operator
    
    def counting_sort(iterable, key):
        positions = key_positions(iterable, key)
        return sorted_array(iterable, key, positions)
        
    objects = [("a", 88), ("b", 17), ("c", 17), ("d", 7)]
    
    key = operator.itemgetter(1)
    print(", ".join(object[0] for object in counting_sort(objects, key)))    