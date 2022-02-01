def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    # solution:
    #     if command == "remove":
    #     if location == "end":
    #         return lst.pop()
    #     elif location == "beginning":
    #         return lst.pop(0)

    # elif command == "add":
    #     if location == "beginning":
    #         lst.insert(0, value)
    #         return lst
    #     elif location == "end":
    #         lst.append(value)
    #         return lst

    if command in ['add', 'remove'] and location in ['end', 'beginning']:
        obj = {
            ("remove", "beginning"): lambda l: l[1:],
            ("remove", "end"): lambda l: l[:-1],
            ("add", "beginning"): lambda l, v: [v]+l,
            ("add", "end"): lambda l, v: l+[v],
        }

        return obj[(command, location)](lst, value) if value else obj[(command, location)](lst)
    else:
        return None


print(list_manipulation([1, 2, 3], 'remove', 'end'))  # [1,2]
print(list_manipulation([1, 2, 3], 'remove', 'beginning'))  # [2,3]
print(list_manipulation([1, 2, 3], 'add', 'beginning', 20))  # [20, 1, 2, 3]
print(list_manipulation([1, 2, 3], 'add', 'end', 30))  # [1, 2, 3, 30]
print(list_manipulation([1, 2, 3], 'foo', 'end'))  # None
print(list_manipulation([1, 2, 3], 'add', 'dunno'))  # None
