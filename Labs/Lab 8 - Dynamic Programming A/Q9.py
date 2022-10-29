import numpy as np

def coins_reqd(value, coinage):
    """Returns coins needed to get value."""
    numCoins = np.array([[0, {}] for i in range(value + 1)])
    for amt in range(1, value + 1):
        minimum = None
        for c in coinage:
            if amt >= c:
                coin_count = numCoins[amt - c]  # Num coins required to solve for amt - c and which coins
                if minimum is None or coin_count[0] < minimum:
                    minimum = coin_count[0]
                    coin = c
        numCoins[amt, 1] = numCoins[amt - coin, 1].copy()
        numCoins[amt, 1][coin] = numCoins[amt, 1].get(coin, 0) + 1
        numCoins[amt, 0] = 1 + minimum
    return sorted(numCoins[value][1].items(), reverse=True)

print(coins_reqd(32, [1, 10, 25]))