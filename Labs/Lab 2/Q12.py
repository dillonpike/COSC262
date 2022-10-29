def perms(items):
    """Returns a list containing all strings of the given length over the 
       alphabet alpha in no particular order.
    """
    tuples = []
    perms_helper(items, tuples, [])
    return tuples

def perms_helper(items, tuples, perm):
    if len(perm) == len(items): 
        tuples.append(tuple(perm))
    else:
        for element in items:
            if element not in perm:
                perms_helper(items, tuples, perm+[element])
            
            
for perm in sorted(perms([1, 2, 3])):
    print(perm)