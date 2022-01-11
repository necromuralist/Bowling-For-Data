# python
from collections import namedtuple
from collections.abc import MutableSequence
from dataclasses import dataclass

InsertionOutput = namedtuple("InsertionOutput", ["element_count",
                                                 "comparisons",
                                                 "swaps",
                                                 "elements"])


def insertion_sort(elements: MutableSequence) -> InsertionOutput:
    """Sorts elements using iterative insertion-sort
    
    Args:
     elements: sortable collection of elements
    
    Returns:
     count of elements, comparisons made, swaps made, sorted elements
    """
    comparisons = swaps = 0
    for next_unsorted_cell in range(1, len(elements)):
        thing_to_insert = elements[next_unsorted_cell]

        in_front_of_me, to_the_right = (next_unsorted_cell - 1,
                                        next_unsorted_cell)

        while not (in_front_of_me < 0 or
               elements[in_front_of_me] <= thing_to_insert):
            comparisons += 1
            swaps += 1
            elements[to_the_right] = elements[in_front_of_me]
            in_front_of_me, to_the_right = (in_front_of_me - 1,
                                            in_front_of_me)

        elements[to_the_right] = thing_to_insert
        swaps += 1

    return InsertionOutput(len(elements), comparisons, swaps, elements)
