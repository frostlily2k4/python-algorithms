def longest_common_subsequence(text1, text2):
    """
    Find the Longest Common Subsequence (LCS)
    between two strings.
    """

    m = len(text1)
    n = len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    # Reconstruct LCS
    lcs = []

    i = m
    j = n

    while i > 0 and j > 0:

        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    lcs.reverse()

    return "".join(lcs)


if __name__ == "__main__":

    first = "AGGTAB"
    second = "GXTXAYB"

    result = longest_common_subsequence(first, second)

    print("First String :", first)
    print("Second String:", second)
    print("Longest Common Subsequence:", result)