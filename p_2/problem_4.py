def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    index_current = 0
    index_zero = 0
    index_two = len(input_list) - 1

    while index_current <= index_two:
        if input_list[index_current] == 2:
            value = input_list[index_two]
            input_list[index_two] = 2
            input_list[index_current] = value
            index_two -= 1

        elif input_list[index_current] == 0:
            input_list[index_current] = input_list[index_zero]
            input_list[index_zero] = 0
            index_zero += 1
            index_current += 1

        else:
            index_current += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function(
    [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
)
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 0, 1, 0, 2, 1, 0, 1, 2, 0, 2])
test_function([])
test_function([1, 0])
test_function([2])