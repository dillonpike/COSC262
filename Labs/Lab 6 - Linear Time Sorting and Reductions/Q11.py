from Q7 import sorted_array, key_positions

def radix_sort(numbers, d):
    sorted_numbers = numbers[:]
    for i in range(d):
        key = lambda x : x // 10**i % 10
        positions = key_positions(sorted_numbers, key)
        sorted_numbers = sorted_array(sorted_numbers, key, positions)
    return sorted_numbers
        
        
if __name__ == '__main__':
    print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))
    print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
    print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))
    print(radix_sort([31, 22, 131, 44], 3))