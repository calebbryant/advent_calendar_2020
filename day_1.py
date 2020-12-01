from typing import List


def get_sum_multiple(num_list: List[int], target_sum: int) -> int:
    """
    Helper function to iterate through a list of numbers and determine which two numbers, if any, match the sum.
    When determined, the multiple of these two numbers is returned.

    :param num_list: List of integers
    :type num_list: List[int]
    :param target_sum: Target sum of two numbers
    :type target_sum: `int`
    :return: The multiple of the two numbers equallying the target sum.
    """
    num_diff = {}
    for number in num_list:
        if number in num_diff:
            return number * num_diff[number]
        # By calculating the different to hit the target and storing it as the key, we can keep this much
        # more CPU efficient as the list scales by limiting it to a single loop.
        num_diff[target_sum - number] = number


if __name__ == '__main__':
    print(get_sum_multiple(input(), 2020))