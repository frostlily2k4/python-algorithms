def merge_sort(arr):
    """
    Sort a list using the Merge Sort algorithm.

    Args:
        arr (list): List of numbers.

    Returns:
        list: Sorted list.
    """

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    sorted_arr = []

    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):

        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1

    while i < len(left_half):
        sorted_arr.append(left_half[i])
        i += 1

    while j < len(right_half):
        sorted_arr.append(right_half[j])
        j += 1

    return sorted_arr
if __name__ == "__main__":
    numbers = [38, 27, 43, 3, 9, 82, 10]

    print("Original:", numbers)

    sorted_numbers = merge_sort(numbers)

    print("Sorted:", sorted_numbers)