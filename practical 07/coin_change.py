"""
Making Change Problem (Dynamic Programming)

Time Complexity: O(amount * len(coins))

Space Complexity: O(amount)
"""


def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


def main():
    print("Name: Rishi")
    coins = list(map(int, input("Enter coin denominations:\n").split()))
    amount = int(input("Enter target amount: "))

    res = coin_change(coins, amount)
    print("\nMinimum coins required =", res)


if __name__ == "__main__":
    main()
