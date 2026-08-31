"""
Matrix Chain Multiplication (Dynamic Programming)

Time Complexity: O(n^3)

Space Complexity: O(n^2)
"""


def matrix_chain_multiplication(p):
    n = len(p)
    if n <= 2:
        return 0

    dp = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n - 1]


def main():
    n = int(input("Enter number of matrices: "))
    p = list(map(int, input("Enter dimensions:\n").split()))

    print("\nMinimum number of multiplications =", matrix_chain_multiplication(p))


if __name__ == "__main__":
    main()
