"""
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))
"""


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if not isinstance(number, int):
        return None

    if number in [0, 1]:
        return number

    floor, roof = 0, number

    while floor <= roof:
        middle = (floor + roof) // 2

        check_1 = middle ** 2 == number
        check_2 = middle ** 2 <= number < (middle + 1) ** 2
        check_3 = middle ** 2 > number

        if check_1 or check_2:
            return middle
        elif check_3:
            roof = middle
        else:
            floor = middle


print("Pass" if (None == sqrt("a")) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (5 == sqrt(25)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
