def find_pit(seq):
    pit = find_pit_helper(seq, 0, len(seq)-1)
    return pit

def find_pit_helper(seq, start, end):
    if end <= start:
        return start
    else:
        mid = (end-start)//2 + start
        if seq[mid] >= seq[mid+1]:
            start = mid + 1
            pit = find_pit_helper(seq, start, end)
        elif seq[mid] >= seq[mid-1]:
            end = mid
            pit = find_pit_helper(seq, start, end)
        else:
            return mid
    return pit
    


print(find_pit([5, 4, 5]))
print(find_pit([10]))
print(find_pit([10, 7, 5, 4]))
print(find_pit([3, 2, 3]))