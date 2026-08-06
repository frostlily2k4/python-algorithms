def activity_selection(start, finish):
    """
    Select the maximum number of non-overlapping activities
    using the Greedy Algorithm.

    Args:
        start (list): Start times.
        finish (list): Finish times.

    Returns:
        list: Selected activities.
    """

    activities = list(enumerate(zip(start, finish), start=1))

    # Sort by finish time
    activities.sort(key=lambda activity: activity[1][1])

    selected = []

    last_finish = -1

    for activity_id, (start_time, finish_time) in activities:

        if start_time >= last_finish:
            selected.append((activity_id, start_time, finish_time))
            last_finish = finish_time

    return selected


if __name__ == "__main__":

    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]

    result = activity_selection(start, finish)

    print("Selected Activities:\n")

    for activity_id, start_time, finish_time in result:
        print(
            f"Activity {activity_id}: "
            f"Start = {start_time}, Finish = {finish_time}"
        )