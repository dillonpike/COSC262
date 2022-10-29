def longest_common_subsequence(list1, list2):
    if len(list1) == 0 or len(list2) == 0:
        return []
    elif list1[-1] == list2[-1]:
        return longest_common_subsequence(list1[:-1], list2[:-1]) + [list1[-1]]
    else:
        soln1 = longest_common_subsequence(list1[:-1], list2)
        soln2 = longest_common_subsequence(list1, list2[:-1])
        if len(soln1) > len(soln2):
            return soln1
        else: 
            return soln2


list1 = [19, 5, 5, 0, 13, 5, 0, 1, 14, 7, 21, 1]
list2 = [19, 5, 5, 0, 20, 8, 5, 0, 7, 21, 19]
print(longest_common_subsequence(list1, list2))

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(longest_common_subsequence(list1, list2))

list1 = [1, -1, 3, 5, 7, 9, 5, 3, 2, 11]
list2 = [1, -1, 3, 5, 7, 9, 5, 3, 2, 11]
print(longest_common_subsequence(list1, list2))