# python
from collections.abc import MutableSequence, Sequence

INFINITY = float("inf")


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

def merge_clrs(collection: MutableSequence,
               left_start: int,
               left_end: int,
               right_end: int) -> int:
    """Merge the sub-sections from the collection

    Args:
     collection: list or array with sorted sub-sections
     left_start: index of start of first sub-section
     left_end: index of last item of first sub-section
     right_end: index of the last item of second sub-section
    """
    count = 0
    left_size = left_end - left_start + 1
    right_size = right_end - left_end
    right_start = left_end + 1

    left_stack = ([None] * left_size)
    right_stack = ([None] * right_size)
    
    for stack_location in range(left_size):
        left_stack[stack_location] = collection[left_start + stack_location]
        count += 1
        
    for stack_location in range(right_size):
        right_stack[stack_location] = collection[right_start + stack_location]
        count += 1

    left_stack.append(INFINITY)
    right_stack.append(INFINITY)

    next_left = next_right = 0

    for put_next_item_here in range(left_start, right_end + 1):
        count += 1
        if left_stack[next_left] <= right_stack[next_right]:
            collection[put_next_item_here] = left_stack[next_left]
            next_left += 1
        else:
            collection[put_next_item_here] = right_stack[next_right]
            next_right += 1
    return count
