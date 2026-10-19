"""
Travelling Salesman Problem (Dynamic Programming)

Time Complexity: O(n^2 * 2^n)

Space Complexity: O(n * 2^n)
"""

INF = float("inf")


def tsp(mask, pos, n, cost, dp):
    if mask == (1 << n) - 1:
        return cost[pos][0] if cost[pos][0] > 0 else (0 if n == 1 else INF)

    if dp[mask][pos] != -1:
        return dp[mask][pos]

    ans = INF
    for nxt in range(n):
        if not (mask & (1 << nxt)):
            if cost[pos][nxt] > 0 and cost[pos][nxt] != INF:
                new_cost = cost[pos][nxt] + tsp(mask | (1 << nxt), nxt, n, cost, dp)
                if new_cost < ans:
                    ans = new_cost

    dp[mask][pos] = ans
    return ans


def main():
    print("Name: Rishi")
    n = int(input("Enter number of cities: "))

    print("Enter cost matrix:")
    cost = []
    for _ in range(n):
        row = [INF if x.upper() == "INF" else int(x) for x in input().split()]
        cost.append(row)

    dp = [[-1] * n for _ in range(1 << n)]
    ans = tsp(1, 0, n, cost, dp)

    print("\nMinimum Cost =", ans)


if __name__ == "__main__":
    main()
