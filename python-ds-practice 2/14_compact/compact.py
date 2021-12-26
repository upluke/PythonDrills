def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    i = 0
    while i < len(lst):
        if not lst[i]:
            lst.remove(lst[i])
        else:
            i += 1
    return lst


print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
