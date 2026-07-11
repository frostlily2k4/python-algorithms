def binary_search(arr, target):
    """
    Perform binary search on a sorted list.

    Args:
        arr (list): Sorted list of values.
        target: Value to search.

    Returns:
        int: Index of target if found, otherwise -1.
    """

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


if __name__ == "__main__":

    numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72]

    target = 23

    result = binary_search(numbers, target)

    if result != -1:
        print(f"{target} found at index {result}")
    else:
        print("Element not found")