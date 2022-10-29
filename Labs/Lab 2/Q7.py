def all_pairs(list1, list2, index=0):
    tuples = []
    if index == len(list1):
        pass
    else:
        tuples += all_pairs_helper(list1[index], list2)
        tuples += all_pairs(list1, list2, index+1)
    return tuples

def all_pairs_helper(list1_el, list2, index=0):
    if index == len(list2):
        return []
    else:
        return [(list1_el, list2[index])] + all_pairs_helper(list1_el, list2, index+1)
    
print(all_pairs([1, 2], [10, 20, 30]))