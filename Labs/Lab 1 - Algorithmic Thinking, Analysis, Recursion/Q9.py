def almost_all(numbers):
    total = sum(numbers)
    return [total - x for x in numbers] 
    
print(almost_all([1,2,3]))
almost_all(list(range(10**5)))
print("OK")