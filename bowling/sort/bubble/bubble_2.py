def bubble(elements) -> Counts:
    """Sorts the list in place

    Args:
     elements: list of (in-place) sortable elements

    Returns:
     number of elements, count of comparisons, count of swaps
    """
    all_but_one = len(elements) - 1
    comparisons = swaps = 0
    for items_bubbled_up in range(all_but_one):
        swapped_at_least_once = False
        for left_hand in range(all_but_one - items_bubbled_up):
            comparisons += 1
            right_hand = left_hand + 1
            if elements[right_hand] < elements[left_hand]:
                (elements[left_hand],
                 elements[right_hand]) = (elements[right_hand],
                                          elements[left_hand])
                swaps += 1
                swapped_at_least_once = True
        if not swapped_at_least_once:
            break
    return (len(elements), comparisons, swaps)
