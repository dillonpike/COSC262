def change_greedy(amount, coinage):
    coins = coinage[:]
    coins.sort()
    coins.reverse()
    change = []
    for coin in coins:
        num = 0
        while coin <= amount:
            amount -= coin
            num += 1
        if num > 0:
            change.append((num, coin))
    if amount == 0:
        return change
    
print(change_greedy(82, [1, 10, 25, 5]))
print(change_greedy(80, [1, 10, 25]))
print(change_greedy(101, [10, 25, 5]))