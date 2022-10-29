def old_sort_of(numbers): 
    result = [] 
    for i in range(len(numbers)): 
        sub = sorted(numbers[i:]) 
        result.append(sub[0]) 
    return result

def better_sort_of(numbers):
    result = []
    copy = numbers[:]
    copy.reverse()
    for i in range(len(numbers)):
        result.append(min(copy))
        copy.pop()
    return result

def sort_of(numbers):
    result = []
    num_dict = {}
    for i in range(len(numbers)):
        num_dict[numbers[i]] = num_dict.get(numbers[i], []) + [i]
    copy = sorted(numbers)
    copy.reverse()
    for i in range(len(numbers)):
        if copy[-1] in num_dict:
            result.append(copy[-1])
            
            
def sort_of(numbers): 
    result = []
    copy = sorted(numbers)
    copy.reverse()
    #print("copy:", copy)
    num_dict = {}
    for i in range(len(numbers)):
        num_dict[numbers[i]] = i
    #print(num_dict)
    for i in range(len(numbers)):
        while i > num_dict[copy[-1]]:
            #print(copy[-1], numbers[i])
            copy.pop()
            #print("copy:", copy, i)
        result.append(copy[-1])  
    return result

print(old_sort_of([1, 2, 3, 3]))
print(old_sort_of([1, 3, 2, 5]))
print(sort_of([1, 2, 3, 3]))
print(sort_of([1, 3, 2, 5]))
sort_of(list(range(10**5)))
print("OK")

nums = [1, 6, 2,9, 123, 0, 23, 5, 7, 1, 2, 5, 6, 23, 16, 16]
if old_sort_of(nums) == sort_of(nums):
    print("WOO!")
    

import time
import math
small = 7
big = 7**300
start = time.time()
math.sqrt(small)
end = time.time()
print(end - start)

start = time.time()
math.sqrt(big)
end = time.time()
print(start)
print(end)
print(end - start)