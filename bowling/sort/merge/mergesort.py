# python
from collections.abc import MutableSequence, Sequence


def merge(left_stack: Sequence,
          right_stack: Sequence,
          target: MutableSequence) -> int:
    """Merges values from left and right stacks into target collection

    Args:
     left_stack: sorted collection of items to merge
     right_stack: sorted collection of items to merge
     target: collection into which to merge the items

    Returns:
     count of basic operations
    """
    left_size, right_size = len(left_stack), len(right_stack)
    next_left = next_right = put_item_here = count = 0
    
    while next_left < left_size and next_right < right_size:
        count += 1
        if left_stack[next_left] <= right_stack[next_right]:
            target[put_item_here] = left_stack[next_left]
            next_left += 1
        else:
            target[put_item_here] = right_stack[next_right]
            next_right += 1

        put_item_here += 1
        
    if next_left == left_size and next_right < right_size:
        for stack_offset in range(left_size + right_size - put_item_here):
            count += 1
            target[put_item_here + stack_offset] = right_stack[next_right + stack_offset]
    elif next_left < left_size:
        for stack_offset in range(left_size + right_size - put_item_here):
            count += 1
            target[put_item_here + stack_offset] = left_stack[next_left + stack_offset]
    return count


def mergesort(collection: MutableSequence) -> int:
    """Sorts the collection using a recursive mergesort

    Args:
     collection: a mutable sequence

    Returns:
     runtime count
    """
    items = len(collection)
    count = 0
    if items > 1:
        middle = items//2
        left_stack = collection[:middle]
        right_stack = collection[middle:]
        assert len(left_stack) + len(right_stack) == items
        count += mergesort(left_stack)
        count += mergesort(right_stack)
        count += merge(left_stack, right_stack, collection)
    return count
