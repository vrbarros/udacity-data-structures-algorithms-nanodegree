"""
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime 
complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
"""


def get_pivot_index(input_list, number):
    i = 0
    length = len(input_list)

    while input_list[i] < input_list[i + 1]:
        i += 1

        if i + 1 == length:
            i = length // 2
            break

    i += 1

    if number in input_list[:i]:
        pivot = len(input_list[:i]) // 2
    else:
        pivot = i + (len(input_list[i:]) // 2)

    return i, pivot


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    length = len(input_list)
    i, pivot = get_pivot_index(input_list, number)

    while input_list[pivot] != number:
        if pivot == i:
            return -1

        if input_list[pivot] < number:
            pivot += 1
        else:
            pivot -= 1

        if pivot < 0 or pivot >= length:
            return -1

    return pivot


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]

    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 1, 2, 3, 4], -1])
test_function([[6, 7, 8, 1, 2, 3, 4, 5], 100])
