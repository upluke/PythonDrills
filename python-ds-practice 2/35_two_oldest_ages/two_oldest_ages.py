def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.

    # solution:

    # 1. find two oldest by sorting unique; this is O(n log n)
    # uniq_ages = set(ages)
    # oldest = sorted(uniq_ages)[-2:]
    # return tuple(oldest)

    # 2. a longer, but O(n) runtime would be:

    # uniq_ages = set(ages)
    # oldest = None
    # second = None

    # for age in uniq_ages:
    #     if oldest is None or age > oldest:
    #         second = oldest
    #         oldest = age
    #     elif second is None or age > second:
    #         second = age

    # return (second, oldest)

    # my solution1:
    # return sorted(set(ages))[-2:]
    # my solution2:
    current_max, return_num2 = 0, max(ages)
    for age in ages:
        if age > current_max and age != return_num2:
            current_max = age
    return (current_max, return_num2)


print(two_oldest_ages([1, 2, 10, 8]))
print(two_oldest_ages([6, 1, 9, 10, 4]))
print(two_oldest_ages([1, 5, 5, 2]))
