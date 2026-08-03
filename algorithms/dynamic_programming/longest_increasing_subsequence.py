def longest_increasing_subsequence(arr):
    """
    Find the Longest Increasing Subsequence (LIS)
    using Dynamic Programming.

    Args:
        arr (list): Input array.

    Returns:
        tuple: Length of LIS and the subsequence.
    """

    n = len(arr)

    if n == 0:
        return 0, []

    dp = [1] * n
    previous = [-1] * n

    for i in range(n):
        for j in range(i):

            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                previous[i] = j

    max_length = max(dp)
    index = dp.index(max_length)

    lis = []

    while index != -1:
        lis.append(arr[index])
        index = previous[index]

    lis.reverse()

    return max_length, lis


if __name__ == "__main__":

    numbers = [10, 22, 9, 33, 21, 50, 41, 60]

    length, sequence = longest_increasing_subsequence(numbers)

    print("Array:")
    print(numbers)

    print("\nLength of LIS:", length)
    print("Longest Increasing Subsequence:", sequence)