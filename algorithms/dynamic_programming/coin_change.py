def coin_change(coins, amount):
    """
    Find the minimum number of coins required
    to make a given amount.

    Args:
        coins (list): Available coin denominations.
        amount (int): Target amount.

    Returns:
        int: Minimum number of coins, or -1 if impossible.
    """

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):

        for coin in coins:

            if coin <= value:
                dp[value] = min(
                    dp[value],
                    dp[value - coin] + 1
                )

    if dp[amount] == float("inf"):
        return -1

    return dp[amount]


if __name__ == "__main__":

    coins = [1, 2, 5]
    amount = 11

    minimum = coin_change(coins, amount)

    print("Coins:", coins)
    print("Target Amount:", amount)

    print("\nMinimum Coins Required:")
    print(minimum)