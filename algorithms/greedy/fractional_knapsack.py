class Item:
    """
    Represents an item with value and weight.
    """

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    @property
    def ratio(self):
        return self.value / self.weight


def fractional_knapsack(capacity, items):
    """
    Solve the Fractional Knapsack Problem
    using a Greedy Algorithm.

    Args:
        capacity (int): Maximum knapsack capacity.
        items (list): List of Item objects.

    Returns:
        float: Maximum obtainable value.
    """

    items.sort(key=lambda item: item.ratio, reverse=True)

    total_value = 0.0

    for item in items:

        if capacity == 0:
            break

        if item.weight <= capacity:

            capacity -= item.weight
            total_value += item.value

        else:

            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0

    return total_value


if __name__ == "__main__":

    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30)
    ]

    capacity = 50

    maximum_value = fractional_knapsack(capacity, items)

    print("Knapsack Capacity:", capacity)

    print(f"\nMaximum Value: {maximum_value:.2f}")
    