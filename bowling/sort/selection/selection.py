from collections.abc import MutableSequence
from collections import namedtuple
from typing import Any, Dict
SelectionOutput = namedtuple("SelectionOutput",
                             ["element_count",
                              "comparisons",
                              "swaps",
                              "elements"])
Swaps = Dict[int, list[int]]
Sortable = MutableSequence[Any]

def selection_counter(elements: Sortable) -> SelectionOutput:
    """Does the selection sort on the elements

    Args:
     elements: list of orderable objects

    Returns:
     (number of elements, comparisons, swaps)
    """
    number_of_elements = len(elements)
    comparisons = swaps = 0
    
    for start_of_unselected in range(number_of_elements - 1):
        smallest_unselected = start_of_unselected
        for next_unselected in range(start_of_unselected + 1,
                                     number_of_elements):
            comparisons += 1
            if elements[next_unselected] < elements[smallest_unselected]:
                smallest_unselected = next_unselected
        swaps += 1
        elements[start_of_unselected], elements[smallest_unselected] = (
            elements[smallest_unselected], elements[start_of_unselected]
        )
    return SelectionOutput(element_count=number_of_elements,
                           comparisons=comparisons,
                           swaps=swaps,
                           elements=elements)

def selection_swaps(elements: Sortable) -> Swaps:
    """Keeps track of the element indexes as they are swapped

    Args:
     elements: list of orderable elements

    Returns:
     dict mapping element to list of indices where it was in the elements list
    """
    swaps = {element: [index] for index, element in enumerate(elements)}

    number_of_elements = len(elements)

    for start_of_unselected in range(number_of_elements - 1):
        smallest_unselected = start_of_unselected

        for next_unselected in range(start_of_unselected + 1,
                                     number_of_elements):
            if elements[next_unselected] < elements[smallest_unselected]:
                smallest_unselected = next_unselected
        
        elements[start_of_unselected], elements[smallest_unselected] = (
            elements[smallest_unselected], elements[start_of_unselected]
        )

        # record the location of the elements
        for index, element in enumerate(elements):
            swaps[element].append(index)
    return swaps
