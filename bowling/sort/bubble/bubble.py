# python standard library
from collections.abc import MutableSequence
from collections import namedtuple

ElementCount = int
ComparisonCount = int
SwapCount = int
SortedElements = MutableSequence

Counts = tuple[ElementCount, ComparisonCount, SwapCount, SortedElements]

IndexHistory = list[int]
ElementValue = int

Swaps = dict[ElementValue, IndexHistory]
BubbleOutput = namedtuple("BubbleOutput",
                          [
                              "element_count", "comparisons",
                              "swaps",
                              "elements"])


def bubba(elements: MutableSequence) -> Counts:
    """Sorts the list in place and tracks the number of comparisons

    Although this is an in-place sort, not all of the sorting methods
    will be so to make it consistent I'm going to always return the
    sorted list


    Args:
     elements: list of (in-place) sortable elements

    Returns:
     number of elements, count of comparisons, count of swaps elements
    """
    all_but_one = len(elements) - 1
    comparisons = swaps = 0
    for items_sorted in range(all_but_one):
        swapped_at_least_once = False
        for in_front_of_us in range(all_but_one - items_sorted):
            comparisons += 1
            to_the_right = in_front_of_us + 1
            if elements[to_the_right] < elements[in_front_of_us]:
                (elements[in_front_of_us],
                 elements[to_the_right]) = (elements[to_the_right],
                                            elements[in_front_of_us])
                swaps += 1
                swapped_at_least_once = True
        if not swapped_at_least_once:
            break
    return (len(elements), comparisons, swaps, elements)


def bubble(elements: MutableSequence) -> Counts:
    """Sorts the list in place

    Args:
     elements: list of (in-place) sortable elements

    Returns:
     number of elements, count of comparisons, count of swaps, sorted elements
    """
    all_but_one = len(elements) - 1
    comparisons = swaps = 0
    for items_sorted in range(all_but_one):
        for in_front_of_us in range(all_but_one - items_sorted):
            comparisons += 1
            to_the_right = in_front_of_us + 1
            if elements[to_the_right] < elements[in_front_of_us]:
                (elements[in_front_of_us],
                 elements[to_the_right]) = (elements[to_the_right],
                                            elements[in_front_of_us])
                swaps += 1
    return BubbleOutput(len(elements), comparisons, swaps, elements)


def swap_tracker(elements: MutableSequence) -> Swaps:
    """Does the bubble-sort and tracks the locations

    Args:
     elements: list of orderable items

    Returns:
     dict of element value: list of indices it was at during sort
    """
    all_but_one = len(elements) - 1

    swaps = {element: [index] for index, element in enumerate(elements)}

    for items_sorted in range(all_but_one):
        for in_front_of_us in range(all_but_one - items_sorted):
            to_the_right = in_front_of_us + 1
            if elements[to_the_right] < elements[in_front_of_us]:
                (elements[in_front_of_us],
                 elements[to_the_right]) = (elements[to_the_right],
                                            elements[in_front_of_us])
                for index, element in enumerate(elements):
                    swaps[element].append(index)
    return swaps
