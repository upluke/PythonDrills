def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    most_count = 0
    for num in nums:
        if most_count < nums.count(num):
            nums[0], num = num, nums[0]

    return nums.pop(0)


print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))
