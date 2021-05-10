def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    assert len(ints) > 0

    min = ints[0]
    max = min

    for i in range(0, len(ints)):
        num = ints[i]

        if num < min:
            min = num

        if num > max:
            max = num

    return min, max


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
print("Pass" if ((0, 0) == get_min_max([0, 0])) else "Fail")
print("Pass" if ((-1, 0) == get_min_max([0, -1])) else "Fail")

l = [i for i in range(0, 500)]  # a list containing 0 - 499
random.shuffle(l)

print("Pass" if ((0, 499) == get_min_max(l)) else "Fail")
