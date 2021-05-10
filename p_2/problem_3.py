"""
Rearrange Array Elements so as to form two number such that their sum is maximum. 
Return these two numbers. You can assume that all array elements are in the range [0, 9]. 
The number of digits in both the numbers cannot differ by more than 1. 
You're not allowed to use any sorting function that Python provides and the expected 
time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. 
In scenarios such as these when there are more than one possible answers, return any one.
"""


def set_cache(input_list):
    cache = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for number in input_list:
        cache[number] += 1

    return cache


def is_odd(length):
    if length % 2 == 0:
        return False
    else:
        return True


def mergesort(arr):
    if len(arr) <= 1:
        return arr

    middle_i = len(arr) // 2
    left_arr = arr[:middle_i]
    right_arr = arr[middle_i:]

    left_arr = mergesort(left_arr)
    right_arr = mergesort(right_arr)

    return merge(left_arr, right_arr)


def merge(left, right):
    result_arr = []
    right_i = 0
    left_i = 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] > right[right_i]:
            result_arr.append(right[right_i])
            right_i += 1
        else:
            result_arr.append(left[left_i])
            left_i += 1

    result_arr += left[left_i:]
    result_arr += right[right_i:]

    return result_arr


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    length = len(input_list)
    arr_sorted = mergesort(input_list)

    if length <= 1:
        return [1, 1]

    odd = is_odd(length)
    cache = set_cache(arr_sorted)

    num_1 = []
    num_2 = []

    for i in range(9, -1, -1):
        while cache[i]:
            if odd:
                num_1.append(str(i))
                odd = False
            else:
                num_2.append(str(i))
                odd = True
            cache[i] -= 1

    result_1 = int("".join(num_1))
    result_2 = int("".join(num_2))

    return [result_1, result_2]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_function([[], [1, 1]])
test_function([[3, 1, 5, 4], [41, 53]])
test_function([[1, 3, 5, 4], [41, 53]])
test_function([[1, 3, 4, 5], [41, 53]])
test_function([[1], [1, 1]])
test_function([[1, 1, 1, 3], [11, 31]])