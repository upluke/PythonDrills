def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    # solution:
    # count = 0

    # for p in parens:
    #     if p == '(':
    #         count += 1
    #     elif p == ')':
    #         count -= 1

    #     # fast fail: too many right parens
    #     if count < 0:
    #         return False

    # return count == 0

    open_paranthesis = []
    for parant in parens:
        if parant == '(':
            open_paranthesis.append(parant)
        else:
            if len(open_paranthesis):
                open_paranthesis.pop()
            else:
                return False
    return True if len(open_paranthesis) == 0 else False
