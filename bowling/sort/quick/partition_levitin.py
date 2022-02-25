# python
from collections.abc import MutableSequence


def partition_levitin(collection: MutableSequence,
                      left: int, right: int) -> int:
    """Partitions the collection using a variation of Hoare's method

    Args:
     collection: the list to partition
     left: index of the first element in the sub-list to partition
     right: index of the last element in the sub-list to partition

    Returns:
     the index of the pivot element
    """
    pivot_element = collection[left]
    partition_left = left
    partition_right = right + 1
    
    while True:
        # if the pivot element is the largest element this loop
        # will try to go past the end of the list so we need a
        # a check in the loop before we increment the partition_left
        while partition_left < right:
            partition_left += 1
            if collection[partition_left] >= pivot_element:
                break

        while True:
            partition_right -= 1
            if collection[partition_right] <= pivot_element:
                break

        if partition_left >= partition_right:
            break

        collection[partition_left], collection[partition_right] = (
            collection[partition_right], collection[partition_left]
        )

    # move the pivot element from the far left to its final place
    collection[left], collection[partition_right] = (
        collection[partition_right], collection[left]
    )

    return partition_right
