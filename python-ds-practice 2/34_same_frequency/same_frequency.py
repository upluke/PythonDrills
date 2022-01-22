def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    hp = {}
    for n in str(num1)+str(num2):
        hp[n] = hp.get(n, 0)+1
    for value in hp.values():
        if value % 2 == 1:
            return False
    return True


print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
