def matrix_chain_order(dimensions):
    """
    Find the minimum number of scalar multiplications
    needed to multiply a chain of matrices.

    Args:
        dimensions (list): Matrix dimensions.

    Returns:
        int: Minimum multiplication cost.
    """

    n = len(dimensions) - 1

    dp = [[0] * n for _ in range(n)]

    for chain_length in range(2, n + 1):

        for i in range(n - chain_length + 1):

            j = i + chain_length - 1

            dp[i][j] = float("inf")

            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + dimensions[i]
                    * dimensions[k + 1]
                    * dimensions[j + 1]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]


if __name__ == "__main__":

    dimensions = [40, 20, 30, 10, 30]

    minimum_cost = matrix_chain_order(dimensions)

    print("Matrix Dimensions:")
    print(dimensions)

    print("\nMinimum Multiplication Cost:")
    print(minimum_cost)