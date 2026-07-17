def quick_sort(arr):
    """
    Sort a list using the Quick Sort algorithm.

    Args:
        arr (list): List of numbers.

    Returns:
        list: Sorted list.
    """

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":

    numbers = [38, 27, 43, 3, 9, 82, 10]

    print("Original:", numbers)

    sorted_numbers = quick_sort(numbers)

    print("Sorted:", sorted_numbers)