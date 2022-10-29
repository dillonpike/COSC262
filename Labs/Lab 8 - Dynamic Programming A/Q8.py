def coins_reqd(value, coinage):
    """The minimum number of coins to represent value assuming a 1-unit coin"""
    num_coins = [0] * (value + 1)
    for amt in range(1, value + 1):
        num_coins[amt] = 1 + min(num_coins[amt - c] for c in coinage if amt >= c)

    # The value of the num_coins array is displayed at this point.
    return num_coins[value]

print(coins_reqd(19, [1, 5, 7, 11]))