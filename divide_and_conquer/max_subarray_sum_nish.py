"""
Given a array of length n, max_subarray_sum() finds
the maximum of sum of contiguous sub-array using divide and conquer method.

Time complexity : O(n log n)

Ref : INTRODUCTION TO ALGORITHMS THIRD EDITION
(section : 4, sub-section : 4.1, page : 70)

"""

from typing import Tuple
from numbers import Number


def max_sum_from_start(array):
    """This function finds the maximum contiguous sum of array from 0 index

    Parameters :
    array (list[int]) : given array

    """
    array_sum = 0
    max_sum = float("-inf")
    idx = 0
    for i, num in enumerate(array):
        array_sum += num
        if array_sum > max_sum:
            max_sum = array_sum
            idx = i
    return (idx, max_sum)


def max_cross_array_sum(array, left, mid, right):
    """This function finds the maximum contiguous sum of left and right arrays

    Parameters :
    array, left, mid, right (list[int], int, int, int)

    """

    left_idx, max_sum_of_left = max_sum_from_start(array[left : mid + 1][::-1])
    left_idx = mid - left_idx
    right_idx, max_sum_of_right = max_sum_from_start(array[mid + 1 : right + 1])
    right_idx += mid + 1
    return (left_idx, right_idx, max_sum_of_left + max_sum_of_right)


def max_subarray_sum(array, left, right) -> Tuple[int, int, Number]:
    """Maximum contiguous sub-array sum, using divide and conquer method

    Parameters :
    array, left, right (list[int], int, int) :
    given array, current left index and current right index

    Returns :
        tuple(int, int, Number)

        (low_index, high_index, sum)

    """

    # base case: array has only one element
    if left == right:
        return (left, right, array[right])

    # Recursion
    mid = (left + right) // 2
    left_low, left_high, left_half_sum = max_subarray_sum(array, left, mid)
    right_low, right_high, right_half_sum = max_subarray_sum(array, mid + 1, right)
    cross_low, cross_high, cross_sum = max_cross_array_sum(array, left, mid, right)

    if left_half_sum >= right_half_sum and left_half_sum >= cross_sum:
        return (left_low, left_high, left_half_sum)
    elif right_half_sum >= left_half_sum and right_half_sum >= cross_sum:
        return (right_low, right_high, right_half_sum)
    else:
        return (cross_low, cross_high, cross_sum)


def main():
    array = [-2, -5, 6, -2, -3, 1, 5, -6]
    array = [0, 1, 0, 2, -3, 3]
    array_length = len(array)

    low, high, s = max_subarray_sum(array, 0, array_length - 1)

    print(f"({low}, {high}) | array -> {array[low:high+1]} | sum -> {s}")


if __name__ == "__main__":
    main()
